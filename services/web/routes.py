from app_directory import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html')
