FROM python:3.10-alpine

ARG APP_USER=newsbot

RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER

USER $APP_USER

ENV PATH "${PATH}:/home/${APP_USER}/.local/bin"

WORKDIR /home/${APP_USER}/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
