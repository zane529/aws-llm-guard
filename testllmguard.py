# -*- coding: utf-8 -*-


from llm_guard.vault import Vault

vault = Vault()

from llm_guard.input_scanners import Anonymize
from llm_guard.input_scanners.anonymize_helpers import BERT_ZH_NER_CONF

scanner = Anonymize(vault, preamble="Insert before prompt", allowed_names=["John Doe"], hidden_names=["Test LLC"],
                    recognizer_conf=BERT_ZH_NER_CONF, language="zh")

output = """患者: 李煊国,男,40岁,手机：189-123-4567,邮箱: test1@amazon.com,自感呼吸困难5年余。患者5年来,每天总感到气出不上来,稍干重活即呼气困难,无咳嗽、咳痰、无略血、无胸痛。在多家医院就诊,心、肺功能均正常。吃补中益气丸稍轻,服多位老中医中药均无效。在当地十大名中医基本都看过。
2009年6月13日患试试药心理前来就诊,面色苍黑,说话前半句有力,后半句无力,牙齿黑黄,舌质粗糙,舌尖红,中苔黄糊,舌根白赤,肺脉滑实有力,右关苦,右尺沉细,左寸浮细而软,左关滑。
诊断:气阳(肺实质虚气阳)。分析:张锡纯治疗大气下陷为开山鼻祖,其升陆汤本人研究多年,此病人有大气下陷的病机,但病机并非如此简单。诊问病史,有吸烟10年的历史,每早咳痰一口,结合脉象,推断病人肺中粘膜之疾较多,肺气升之受阻,肝气又受都金所克,大气有降无升。单纯提气,难能如愿。
治疗:养肺阴,清肺腑,补肺助运,疏肝泄胆。
处方:女参30 生牡蛎20 百合20 黄芩15
葛根20 白术20 茯苓20 柴胡15 枳实15
竹茹15 郁金20 黄芪25 川断20
五付
患者服完两副,即感肺中轻松,出气顺畅,劳累后稍有加重,五付后复诊,出气困难未在复发,嗓哑烟,勿重力劳作。继续服药3付巩固疗效。"""

sanitized_prompt, is_valid, risk_score = scanner.scan(output)
print(sanitized_prompt)
print(is_valid)