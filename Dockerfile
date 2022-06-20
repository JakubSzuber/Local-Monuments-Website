FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

WORKDIR /Local-Monuments-Website

COPY app.py .
# moze daj COPY . /app

COPY requirements.txt /Local-Monuments-Website/requirements.txt

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
