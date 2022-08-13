pq_user = 'admin'
pg_pass = 'admin'
pg_db = 'flask_db'
pg_host = 'flask-database'  # Tutaj moze byc inaczej
pg_port = 5432

DB = f'postgresql://{pq_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
