from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
# p = pipeline('text-generation', 'damo/nlp_gpt3_kuakua-robot_chinese-large')
p = pipeline('text2text-generation', 'ClueAI/ChatYuan-large')
p = pipeline('text-generation', 'ClueAI/ChatYuan-large')
p('今天终于拿到驾照了，求夸',)
p('我想听音乐')
p('早上好')

print("ok")
