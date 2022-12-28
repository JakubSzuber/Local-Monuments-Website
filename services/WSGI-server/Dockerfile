FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY docker-entrypoint.sh /usr/local/bin/

COPY . /app/

#ENTRYPOINT [ "docker-entrypoint.sh" ]

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "-w", "3", "run:app" ]
