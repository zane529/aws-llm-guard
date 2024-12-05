
# -*- coding: utf-8 -*-

from llm_guard.output_scanners import BanSubstrings
from llm_guard.input_scanners.ban_substrings import MatchType

scanner = BanSubstrings(
  substrings=["礼来", "unwanted"],
  match_type=MatchType.WORD,
  case_sensitive=False,
  redact=False,
  contains_all=False,
)
sanitized_output, is_valid, risk_score = scanner.scan("可的松", "可的松是礼来生产的一种药物，一种广谱性糖皮质激素,主要用于治疗各种炎症性疾病,如关节炎、哮喘、皮肤病等。它可以通过口服或注射的方式给药")
print(sanitized_output)
print(is_valid)