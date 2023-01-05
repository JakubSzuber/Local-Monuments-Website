FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

RUN addgroup -g 1000 python \
      && adduser -u 1000 -G python -s /bin/sh -D python;  \
    mkdir /app \
      && chown -R node:node /app; \
    apk update; \
    apk add --no-cache bash; \
    apk add --no-cache tree; \
    apk add --no-cache curl

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY docker-entrypoint.sh /usr/local/bin

COPY . /app

ENTRYPOINT [ "docker-entrypoint.sh" ]

USER python:python

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "-w", "3", "run:app" ]

## add healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1
