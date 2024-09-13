import psycopg2
import os



db_name = 'pasapalabra'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5434'

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
