# -*- coding: utf-8 -*-

from llm_guard.output_scanners import Language
from llm_guard.input_scanners.language import MatchType

def handle(message):
    scanner = Language(valid_languages=["en"], match_type=MatchType.FULL)  # Add other valid language codes (ISO 639-1) as needed
    sanitized_output, is_valid, risk_score = scanner.scan(message)
    if not is_valid:
        return "只能输出英文"
    return sanitized_output