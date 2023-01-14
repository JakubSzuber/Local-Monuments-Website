# This is a config file for a Flask application
# It sets up variables for the Postgres database connection such as user, password, host, port and database name
# It also creates a connection string for connecting to the database using the set variables

pq_user = "admin"
pg_pass = "admin"
pg_db = "flask_db"
pg_host = "flask-database"
pg_port = 5432

DB = f"postgresql://{pq_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}"
