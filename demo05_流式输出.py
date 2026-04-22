# 导入模型
import os
from openai import OpenAI

messages = [{"role": "system","content": "你是一个反感詹姆斯的人，简洁回答问题"}]
# 创建一个模型对象
client = OpenAI(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
while True:
    question = input('请输入问题：')
    messages.append({"role": "user", "content": question})
    # 调用模型=>发送prompt提示词=>获取结果
    stream = client.chat.completions.create(
        model='qwen-plus',
        messages=messages,
        stream = True,
    )

    # 获取返回结果
    for chunk in stream:
        print(
            chunk.choices[0].delta.content,
            end="",
            flush=True,
        )
