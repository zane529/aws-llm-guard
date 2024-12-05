from llm_guard.input_scanners import Toxicity
from llm_guard.input_scanners.toxicity import MatchType
from llm_guard.input_scanners.toxicity import DEFAULT_MODEL as TOXICITY_MODEL

TOXICITY_MODEL.path = "/home/ubuntu/llm-guard/model/Qwen1.5-4B-Chinese-toxic-content-detection"
TOXICITY_MODEL.kwargs["local_files_only"] = True

scanner = Toxicity(model=TOXICITY_MODEL,threshold=0.5, match_type=MatchType.FULL)


sanitized_prompt, is_valid, risk_score = scanner.scan("我要杀了你")
print(sanitized_prompt)
print(is_valid)