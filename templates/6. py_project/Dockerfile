# установка базового образа (host OS)
FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY requirements.txt /tmp/

COPY . /app

RUN pip install -U pip && pip install -r requirements.txt

ENV NGINX_WORKER_PROCESSES auto

#RUN mkdir -p /usr/src/app/
#WORKDIR /usr/src/app/

## копирование файла зависимостей в рабочую директорию
#COPY . /usr/src/app/

## установка зависимостей
#RUN pip install --no-cache-dir -r requirements.txt

## установка работы с портом
#EXPOSE 80

## команда, выполняемая при запуске контейнера
#CMD [ "python", "main.py" ]