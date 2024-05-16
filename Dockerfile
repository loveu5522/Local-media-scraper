# 使用基础镜像
FROM python:3.9-slim

# 创建一个非 root 用户，并指定 UID 和 GID
RUN groupadd -g 100 myuser && useradd -u 1029 -g myuser myuser

# 设置工作目录
WORKDIR /app

# 设置 /config 目录为卷
VOLUME /config

# 安装所需的依赖
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --no-cache-dir xmltodict

# 切换到新创建的用户
USER myuser

# 运行脚本
CMD ["python", "/config/script.py"]
