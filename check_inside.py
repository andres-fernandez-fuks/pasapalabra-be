import psycopg2
import os



db_name = os.getenv('POSTGRES_DB')
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
host = os.getenv('POSTGRES_HOST')
port = os.getenv('POSTGRES_PORT')

print("Db uri: ", f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

try:
    conn = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cur = conn.cursor()
    cur.execute('SELECT 1')
    print('Database connection successful!')
    conn.close()
except Exception as e:
    print(f'Error connecting to database: {e}')
