# 使用基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 设置 /config 目录为卷
VOLUME /config

# 安装所需的依赖
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --no-cache-dir xmltodict

# 运行脚本
CMD ["python", "/config/script.py"]
