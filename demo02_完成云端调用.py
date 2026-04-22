# 导入模型
import os
from openai import OpenAI

# 创建一个模型对象
client = OpenAI(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
question = input('请输入问题：')
# 调用模型=>发送prompt提示词=>获取结果
completion = client.chat.completions.create(
    model='qwen-plus',
    messages=[
        {"role":"system","content":"你是一个乐于助人的AI机器人，擅长解决各种疑难杂症，能用粗俗的语言回答问题"},
        {"role":"user","content":question}
    ]
)
# 获取返回结果
print(completion.choices[0].message.content)