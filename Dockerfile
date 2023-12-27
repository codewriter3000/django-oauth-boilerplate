FROM python:3.11.3-buster

ENV PYTHONBUFFERED=1

ENV DJANGO_SETTINGS_MODULE='config.settings.prod'

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x .

RUN python manage.py shell --settings=$DJANGO_SETTINGS_MODULE

CMD python manage.py runserver 0.0.0.0:8000