# Netlify 部署指南

## 前置准备

1. **注册 Netlify 账号**
   - 访问 https://www.netlify.com/
   - 使用 GitHub/GitLab/Bitbucket 或邮箱注册

2. **准备 API Key**
   - 确保你已经有 DashScope API Key
   - 在阿里云 DashScope 控制台获取: https://dashscope.console.aliyun.com/

## 部署步骤

### 方法一: 通过 Git 仓库部署(推荐)

1. **将代码推送到 Git 仓库**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **在 Netlify 中连接仓库**
   - 登录 Netlify
   - 点击 "Add new site" → "Import an existing project"
   - 选择你的 Git 提供商(GitHub/GitLab/Bitbucket)
   - 选择你的仓库

3. **配置构建设置**
   - Build command: `pip install -r requirements.txt`
   - Publish directory: `.`
   - 点击 "Deploy site"

4. **设置环境变量**
   - 进入 Site settings → Environment variables
   - 添加环境变量:
     - Key: `DASHSCOPE_API_KEY`
     - Value: 你的 DashScope API Key
   - 点击 "Save"

5. **重新部署**
   - 进入 Deploys 标签页
   - 点击 "Trigger deploy" → "Deploy site"

### 方法二: 通过 Netlify CLI 部署

1. **安装 Netlify CLI**
   ```bash
   npm install -g netlify-cli
   ```

2. **登录 Netlify**
   ```bash
   netlify login
   ```

3. **初始化站点**
   ```bash
   netlify init
   ```

4. **设置环境变量**
   ```bash
   netlify env:set DASHSCOPE_API_KEY your_api_key_here
   ```

5. **部署**
   ```bash
   netlify deploy --prod
   ```

### 方法三: 手动拖拽部署

1. **压缩项目文件**
   - 将以下文件打包成 zip:
     - stream_app.py
     - requirements.txt
     - netlify.toml
     - Procfile
     - app.py

2. **上传到 Netlify**
   - 登录 Netlify
   - 进入 "Sites" 页面
   - 将 zip 文件拖拽到上传区域

3. **设置环境变量**
   - 进入 Site settings → Environment variables
   - 添加 `DASHSCOPE_API_KEY`

## 重要提示

⚠️ **注意**: Netlify 主要用于静态网站托管,对 Streamlit 这类需要持续运行的应用支持有限。

### 替代方案推荐

如果 Netlify 部署遇到问题,建议使用以下平台:

1. **Streamlit Cloud**(最推荐)
   - 访问: https://streamlit.io/cloud
   - 直接连接 GitHub 仓库
   - 免费且对 Streamlit 支持最好
   - 设置 Secrets 添加 API Key

2. **Hugging Face Spaces**
   - 访问: https://huggingface.co/spaces
   - 免费 GPU/CPU 资源
   - 支持 Streamlit

3. **Render**
   - 访问: https://render.com/
   - 免费套餐可用
   - 支持 Python Web 应用

4. **Railway**
   - 访问: https://railway.app/
   - 简单的部署流程
   - 有免费额度

## 使用 Streamlit Cloud 部署(强烈推荐)

1. **将代码推送到 GitHub**
   ```bash
   git add .
   git commit -m "Streamlit app"
   git push origin main
   ```

2. **访问 Streamlit Cloud**
   - 打开 https://streamlit.io/cloud
   - 点击 "New app"

3. **配置应用**
   - Repository: 选择你的 GitHub 仓库
   - Branch: main
   - Main file path: stream_app.py

4. **设置 Secrets**
   - 点击 "Advanced settings" → "Secrets"
   - 添加: `DASHSCOPE_API_KEY=你的API密钥`

5. **部署**
   - 点击 "Deploy!"
   - 等待部署完成即可访问

## 故障排查

### 问题: 部署后无法访问
- 检查环境变量是否正确设置
- 查看部署日志确认是否有错误

### 问题: API 调用失败
- 确认 `DASHSCOPE_API_KEY` 已正确配置
- 检查 API Key 是否有效

### 问题: 依赖安装失败
- 检查 requirements.txt 格式
- 尝试更新依赖版本

## 项目文件说明

- `stream_app.py` - Streamlit 应用主文件
- `requirements.txt` - Python 依赖包
- `netlify.toml` - Netlify 配置文件
- `Procfile` - 进程启动文件
- `app.py` - 备用启动入口
