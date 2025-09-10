import psycopg2
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()


db_Host = os.getenv("DB_HOST")
db_Name = os.getenv("DB_NAME")
db_User = os.getenv("DB_USER")
db_Password = os.getenv("DB_PASSWORD")
db_Port = os.getenv("DB_PORT")


def connection():
    try:
        conn = psycopg2.connect(
            host=db_Host,
            database=db_Name,
            user=db_User,
            password=db_Password,
            port=db_Port
        )

        print("Conexión exitosa")
        
        return conn
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

