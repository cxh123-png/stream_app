# 导入模型
import os
from openai import OpenAI
messages = [{"role":"system","content":"你是一个嫉恶如仇的nba评论员，你可以喜欢球技不佳的nba球星，但是必须讨厌品行不端的球员。"}]
# 创建一个模型对象
client = OpenAI(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
while True:
    question = input('请输入问题：')
    messages.append({"role":"user","content":question})
# 调用模型=>发送prompt提示词=>获取结果
    completion = client.chat.completions.create(
        model='qwen-plus',
        messages=messages
    )
# 获取返回结果
    reply = completion.choices[0].message.content
    print("AI:",reply)
    messages.append({"role":"assistant","content":reply})