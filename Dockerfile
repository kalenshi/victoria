FROM python:3.9

ENV PYTHONUNBUFFURED 1

USER root

RUN apt-get update \
    && apt-get  install -y libpq-dev gcc \
    && pip install --upgrade pip \
    && pip install psycopg2
RUN mkdir /app

WORKDIR /app
RUN useradd -m victoria \
    && chown -R victoria:victoria /app
USER victoria

COPY ./requirements.txt ./requirements.txt
COPY ./run.py ./run.py
COPY ./victoria /app/victoria

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "run.py"]

