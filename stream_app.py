import os
import streamlit as st
from openai import OpenAI

# 页面配置
st.set_page_config(
    page_title="AI 聊天助手",
    page_icon="🤖",
    layout="centered"
)

# 标题
st.title("🤖 AI 聊天助手")

# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "你是一个python+ai大模型的面试官。"}
    ]

if "history" not in st.session_state:
    st.session_state.history = []

# 创建模型对象
@st.cache_resource
def init_client():
    return OpenAI(
        api_key=os.getenv('DASHSCOPE_API_KEY'),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

client = init_client()

# 显示聊天历史
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 用户输入
if prompt := st.chat_input("请输入问题："):
    # 显示用户消息
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 添加到历史记录
    st.session_state.history.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 调用模型获取流式响应
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        stream = client.chat.completions.create(
            model='qwen-plus',
            messages=st.session_state.messages,
            stream=True,
        )
        
        # 流式输出
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")
        
        # 显示完整响应
        message_placeholder.markdown(full_response)
        
        # 添加助手响应到历史记录
        st.session_state.history.append({"role": "assistant", "content": full_response})
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# 侧边栏 - 清除对话按钮
with st.sidebar:
    st.header("设置")
    if st.button("清除对话历史"):
        st.session_state.messages = [
            {"role": "system", "content": "你是一个python+ai大模型的面试官"}
        ]
        st.session_state.history = []
        st.rerun()
