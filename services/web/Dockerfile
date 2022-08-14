FROM python:3.10.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

# EXPOSE 5000 ???

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-w", "3", "run:app"]
