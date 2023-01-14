# This is a routes file for a Flask application
# It defines the routing for the home, about, and gallery pages
# It makes use of the get_db_connection function to fetch data from the database
# It also uses the render_template function to render the appropriate html templates

from . import app, get_db_connection  # Import the app and get_db_connection function
from flask import render_template


@app.route("/")
@app.route("/home")
def home_page():
    """
    Handle the request for the home page
    """

    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()

    # Execute a command to select all monuments from the monuments table
    cur.execute("SELECT * FROM monuments;")

    # Fetch all the results
    monuments = cur.fetchall()

    # Close the cursor and connection
    cur.close()
    conn.close()

    # Render the home template and pass the monuments data
    return render_template("home.html", monuments=monuments)


@app.route("/about")
def about_page():
    """
    Handle the request for the about page
    """

    # Render the about template
    return render_template("about.html")


@app.route("/gallery")
def gallery_page():
    """
    Handle the request for the gallery page
    """

    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()

    # Execute a command to select all monuments from the monuments table
    cur.execute("SELECT * FROM monuments;")

    # Fetch all the results
    monuments = cur.fetchall()

    # Close the cursor and connection
    cur.close()
    conn.close()

    # Render the gallery template and pass the monuments data
    return render_template("gallery.html", monuments=monuments)
