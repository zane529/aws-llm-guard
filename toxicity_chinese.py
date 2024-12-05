from __future__ import annotations

from enum import Enum
from llm_guard.model import Model
from llm_guard.transformers_helpers import get_tokenizer_and_model_for_classification, pipeline
from llm_guard.util import calculate_risk_score, get_logger, split_text_by_sentences

from .base import Scanner

LOGGER = get_logger()

DEFAULT_CHINESE_MODEL = Model(
    path="thu-coai/roberta-base-cold",    # 更改为新模型路径
    revision=None,                         # 如果没有特定版本号可以设为 None
    onnx_path=None,                       # 如果没有 ONNX 版本可以设为 None
    onnx_revision=None,
    pipeline_kwargs={
        "padding": "max_length",
        "top_k": None,
        "function_to_apply": "sigmoid",
        "return_token_type_ids": False,
        "max_length": 512,
        "truncation": True,
    },
)


class MatchType(Enum):
    SENTENCE = "sentence"
    FULL = "full"

    def get_inputs(self, prompt: str) -> list[str]:
        if self == MatchType.SENTENCE:
            return split_text_by_sentences(prompt)

        return [prompt]


class Toxicity(Scanner):
    def __init__(
        self,
        *,
        model: Model | None = None,
        threshold: float = 0.5,
        match_type: MatchType | str = MatchType.FULL,
        use_onnx: bool = False
    ) -> None:
        if isinstance(match_type, str):
            match_type = MatchType(match_type)

        self._threshold = threshold
        self._match_type = match_type
        self._use_onnx = use_onnx
        self._model = model
        if self._model is not None:
            model = self._model
        else:
            model = DEFAULT_CHINESE_MODEL

        tf_tokenizer, tf_model = get_tokenizer_and_model_for_classification(
            model=model,
            use_onnx=self._use_onnx,
        )

        self._pipeline = pipeline(
            task="text-classification",
            model=tf_model,
            tokenizer=tf_tokenizer,
            **model.pipeline_kwargs,
        )


    def scan(self, prompt: str) -> tuple[str, bool, float]:
        if prompt.strip() == "":
            return prompt, True, -1.0

        inputs = self._match_type.get_inputs(prompt)
        results_all = self._pipeline(inputs)

        # 中文模型处理逻辑
        highest_toxicity_score = 0.0
        for results_chunk in results_all:
            # 获取预测的标签和得分
            scores = {r["label"]: r["score"] for r in results_chunk}
            # 如果 LABEL_0 的概率更大，说明是安全的
            if scores["LABEL_0"] > scores["LABEL_1"]:
                toxicity_score = 0.0
            else:
                toxicity_score = scores["LABEL_1"]

            highest_toxicity_score = max(highest_toxicity_score, toxicity_score)

        is_safe = highest_toxicity_score <= self._threshold
        if not is_safe:
            LOGGER.warning("Detected offensive content in Chinese text", score=highest_toxicity_score)
        else:
            LOGGER.debug("Text is safe", score=highest_toxicity_score)

        return prompt, is_safe, calculate_risk_score(highest_toxicity_score, self._threshold)