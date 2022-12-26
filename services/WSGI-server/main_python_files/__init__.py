from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from main_python_files.config import DB
import psycopg2

app = Flask(__name__, template_folder='../template')
app.config['SQLALCHEMY_DATABASE_URI'] = DB
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# below func from blog article
def get_db_connection():
    conn = psycopg2.connect(host='flask-database',  # Tutaj moze byc: localhost albo flask-database
                            database='flask_db',
                            user='admin',
                            password='admin',
                            port=5432)
    return conn

from main_python_files import routes
