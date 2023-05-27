FROM python:3.11.1-slim-buster
LABEL maintainer="oleksii.stulen@gmail.com"

WORKDIR /home/www/nifty_tb_bot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r ./requirements.txt

COPY entrypoint.py /usr/local/bin/entrypoint.py

RUN chmod +x /usr/local/bin/entrypoint.py

COPY . .

ENTRYPOINT ["python", "/usr/local/bin/entrypoint.py"]
