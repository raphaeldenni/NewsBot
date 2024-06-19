FROM python:3.12-alpine

ARG APP_USER=newsbot

RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER

USER $APP_USER

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
