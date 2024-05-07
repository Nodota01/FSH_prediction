# 使用 Python 3.11 作为基础镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 将 requirements.txt 复制到容器中的 /app 目录下
COPY requirements.txt /app/

# 安装依赖包
RUN pip install -r requirements.txt

# 将本地的 Python 项目文件复制到容器中的 /app 目录下
COPY . /app/

# 启动容器时运行的命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8123"]
