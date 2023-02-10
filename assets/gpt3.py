from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

#https://modelscope.cn/models/damo/nlp_gpt3_text-generation_chinese-large/quickstart

p = pipeline('text-generation', 'damo/nlp_gpt3_text-generation_chinese-large')
