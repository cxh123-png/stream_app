#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Netlify 部署入口文件
"""
import subprocess
import sys

def main():
    """启动 Streamlit 应用"""
    try:
        # 启动 Streamlit 应用
        subprocess.run([
            sys.executable, 
            "-m", 
            "streamlit", 
            "run", 
            "stream_app.py",
            "--server.port=8501",
            "--server.address=0.0.0.0",
            "--server.headless=true"
        ])
    except Exception as e:
        print(f"Error starting Streamlit: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
