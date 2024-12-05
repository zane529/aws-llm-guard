# -*- coding: utf-8 -*-


from llm_guard.vault import Vault

vault = Vault()

from llm_guard.input_scanners import Anonymize
from llm_guard.input_scanners.anonymize_helpers import BERT_LARGE_NER_CONF
from llm_guard.input_scanners.anonymize_helpers import BERT_ZH_NER_CONF

scanner = Anonymize(vault, preamble="Insert before prompt", allowed_names=["John Doe"], hidden_names=["Test LLC"],
                    recognizer_conf=BERT_ZH_NER_CONF, language="zh")
sanitized_prompt, is_valid, risk_score = scanner.scan("我叫王大，喜欢去旺角餐厅吃牛角包, 今年买了阿里巴巴的股票，亏得舅老爷的裤衩都没了，我的邮箱是 enzec@amazon.com，有好消息发我这个邮箱")
print(sanitized_prompt)
print(is_valid)