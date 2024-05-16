# 使用基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 安装所需的依赖
RUN apt-get update && \
    apt-get install -y cron && \
    apt-get install -y ffmpeg && \
    pip install --no-cache-dir xmltodict

# 复制脚本文件到工作目录
COPY /config/script.py /app/script.py

# 添加 crontab 文件到容器
COPY crontab.txt /etc/cron.d/local-media-scraper-cron

# 启动 cron 服务并输出日志到控制台
CMD service cron start && cron && tail -f /var/log/cron.log
