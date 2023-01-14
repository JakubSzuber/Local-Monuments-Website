# This is an initialization file for a Flask application
# It sets up the Flask app and connects it to a SQLAlchemy object and a Bcrypt object
# It also imports a config file for the database connection URI and sets a secret key for the application
# Additionally, it creates a function for creating a connection to a Postgres database
# It also imports the routes module for the application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .config import DB
import psycopg2

app = Flask(__name__, template_folder="../src/template", static_folder="../src/static")
app.config["SQLALCHEMY_DATABASE_URI"] = DB  # URI for connecting to the database
app.config["SECRET_KEY"] = "ec9439cfc6c796ae2029594d"  # Secret key for the application

db = SQLAlchemy(app)  # SQLAlchemy object connected to the app
bcrypt = Bcrypt(app)  # Bcrypt object connected to the app

# Function to create a connection to the Postgres database
def get_db_connection():
    conn = psycopg2.connect(
        host="flask-database",
        database="flask_db",
        user="admin",
        password="admin",
        port=5432,
    )
    return conn

from . import routes  # Import the routes module
