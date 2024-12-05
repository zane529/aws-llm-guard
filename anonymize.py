# -*- coding: utf-8 -*-

from llm_guard.vault import Vault
from llm_guard.input_scanners import Anonymize
from llm_guard.input_scanners.anonymize_helpers import BERT_ZH_NER_CONF


def handle(message):
    vault = Vault()
    scanner = Anonymize(vault, recognizer_conf=BERT_ZH_NER_CONF, language="zh")
    sanitized_prompt, is_valid, risk_score = scanner.scan(message)
    return sanitized_prompt
