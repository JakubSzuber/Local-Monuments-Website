import os
import psycopg2
from main_python_files import app, get_db_connection  # moze byc tu inaczej
from flask import Flask, render_template

@app.route('/')
@app.route('/home')
def home_page():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM monuments;')
    monuments = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('home.html', monuments=monuments)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html')
