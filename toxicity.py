from llm_guard.input_scanners import Toxicity
from llm_guard.input_scanners.toxicity import MatchType

scanner = Toxicity(threshold=0.5, match_type=MatchType.SENTENCE)
sanitized_prompt, is_valid, risk_score = scanner.scan("我要杀了你")
print(sanitized_prompt)
print(is_valid)