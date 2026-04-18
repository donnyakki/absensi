import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="absensi_greatday",
        user="postgres",
        password="password"
    )
