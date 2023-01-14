## Python lightweight alpine image
FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

## Create the group and user in order to later use a non-root user and give him permission to workdir. Furthermore, install needed commands
RUN addgroup -g 1000 python \
      && adduser -u 1000 -G python -s /bin/sh -D python;  \
    mkdir /app \
      && chown -R python:python /app; \
    apk update; \
    apk add --no-cache bash; \
    apk add --no-cache tree; \
    apk add --no-cache curl

## Use /app as a working directory
WORKDIR /app

## Copy pip dependencies to workdir
COPY requirements.txt /app

## Instal pip dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

## Copy bash script to user's binaries
COPY docker-entrypoint.sh /usr/local/bin

## Copy all files to workdir
COPY . /app

# Execute bash script (that prints some information and initializes the database)
ENTRYPOINT [ "docker-entrypoint.sh" ]

## Switch to non-root user
USER python:python

## Expose port 5000
EXPOSE 5000

# Run Gunicorn service
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "-w", "3", "run:app" ]

## Healthchecks
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1
