FROM python:3.9

WORKDIR /Local-Monuments-Website

COPY app.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

EXPOSE 80
