import os
import psycopg2
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB

# below func from blog article
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user='admin',
                            password='admin')
    return conn

from web import routes
