# 导入模型
import os
from openai import OpenAI

# 创建一个模型对象
client = OpenAI(
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
# 3. 定义系统提示词（给AI一个角色定位）
system_prompt= """
张明远，138-1234-5678
广东省深圳市南山区科技园南区高新南一道1000号腾讯大厦18层 1806室
"""
# 4. 定义用户输入案例
user_prompt_example = """
张明远，138-1234-5678
广东省深圳市南山区科技园南区高新南一道1000号腾讯大厦18层 1806室
"""
# 5. 定义模型返回案例
ai_response_example = """
{
  "name": "张明远",
  "phone": "13812345678",
  "address": "广东省深圳市南山区科技园南区高新南一道1000号腾讯大厦18层 1806室"
}
"""
# 6. 定义用户真正要提取的内容
user_query="""
李婉婷
151-9876-5432
北京市海淀区中关村大街1号海龙大厦8层805室
东西是一份文件，已经封装好了。寄普通快递就行，麻烦寄出后把单号发我一下，谢谢啦！
"""
# 调用模型=>发送prompt提示词=>获取结果
completion = client.chat.completions.create(
    model='qwen-plus',
    messages=[
{'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt_example},
        {'role': 'assistant', 'content': ai_response_example},
        {'role': 'user', 'content': user_query}
    ]
)
# 获取返回结果
print(completion.choices[0].message.content)
