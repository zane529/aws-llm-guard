# -*- coding: utf-8 -*-


from llm_guard.output_scanners import Language
from llm_guard.input_scanners.language import MatchType

scanner = Language(valid_languages=["en"], match_type=MatchType.FULL)  # Add other valid language codes (ISO 639-1) as needed
sanitized_output, is_valid, risk_score = scanner.scan("中文测试", "你的 idea 很好，但是是有问题的")
print(sanitized_output)
print(is_valid)