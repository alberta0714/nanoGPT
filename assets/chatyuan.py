from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

# https://modelscope.cn/models/ClueAI/ChatYuan-large/quickstart
p = pipeline('text2text-generation', 'ClueAI/ChatYuan-large')
p('早上好')
p('今天的天气')
p('你会什么？')
p('你会什么')
p('你是谁？')


