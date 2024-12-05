# -*- coding: utf-8 -*-

from llm_guard.input_scanners import BanCompetitors

competitor_list = ["礼来", "Lilly"]  # Extensive list of competitors
scanner = BanCompetitors(competitors=competitor_list, redact=False, threshold=0.5)
sanitized_prompt, is_valid, risk_score = scanner.scan("帮我介绍一下礼来这家公司")
print(sanitized_prompt)
print(is_valid)