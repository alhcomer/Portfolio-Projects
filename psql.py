from psycopg2 import sql, Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import table
from datetime import datetime, timezone

load_dotenv()

class PostgresManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def open_connection(self):
        self.connection = psycopg2.connect(
            database="my_blog",
            user='postgres',
            password=os.getenv('PSQL_PASSWORD'),
            host='localhost',
            port= '5432'
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("PSQL connection is closed")

    # BELOW METHOD MUST BE EDITED BEFORE USE
    def create_table(self):
        try:
            self.open_connection()
            create_table_query = '''CREATE TABLE IF NOT EXISTS portfolio_posts 
            (id SERIAL PRIMARY KEY NOT NULL,
            title VARCHAR (250) NOT NULL,
            subtitle VARCHAR (250) NOT NULL,
            body TEXT   NOT NULL,
            created_on TIMESTAMP NOT NULL,
            img_url TEXT NOT NULL,
            github_url TEXT)
            '''
            self.cursor.execute(create_table_query)

        except Error as error:
            print("Error while connecting to PSQL", error)

        finally:
            self.close_connection()

    # BELOW METHOD MUST BE EDITED BEFORE USE
    def insert_table_data(self):
        try:
            self.open_connection()
            title = "first blog title"
            subtitle = "first blog subtitle"
            body = "body of the first blog"
            dt = datetime.now(timezone.utc)
            img_url = r"https://upload.wikimedia.org/wikipedia/commons/8/80/Equus_asinus_Kadzid%C5%82owo_001.jpg"
            query = '''INSERT INTO blog_posts (title, subtitle, body, created_on, img_url)
            VALUES (%s, %s, %s, %s, %s) RETURNING id;'''
            self.cursor.execute(query, (title, subtitle, body, dt, img_url))

        except Error as error:
            print("Error while connecting to PSQL", error)

        finally:
            self.close_connection()

    def get_records(self, table_name):
        try:
            self.open_connection()
            query = f'''SELECT * FROM {table_name}'''
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result

        except Error as error:
            print("Error while connecting to PSQL", error)

        finally:
            self.close_connection()


