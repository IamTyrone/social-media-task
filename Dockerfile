FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN apt update -y && apt upgrade -y
RUN apt install gcc -y
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 5000