from flask import Flask
from config import Config
import psycopg2

app = Flask(__name__)
app.config.from_object(Config)

def connect_db():
    try:
        connection = psycopg2.connect(
            user=app.config['POSTGRES_USER'],
            password=app.config['POSTGRES_PASSWORD'],
            host=app.config['POSTGRES_HOST'],
            port=app.config['POSTGRES_PORT'],
            database=app.config['POSTGRES_DB']
        )
        return connection
    except Exception as error:
        print("Error while connecting to PostgreSQL", error)
        return None

@app.route('/')
def index():
    connection = connect_db()
    if connection:
        return "Connected to the database!"
    else:
        return "Failed to connect to the database."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
