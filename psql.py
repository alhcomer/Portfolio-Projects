from psycopg2 import sql, Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import table
from datetime import datetime, timezone

load_dotenv()

# CREATE DATABASE IF ONE DOES NOT EXIST


# FUNCTION TO CREATE NEW TABLES/ QUERY MUST BE EDITED FOR NEW TABLES
def create_table():
    create_table_query = '''CREATE TABLE IF NOT EXISTS portfolio_posts 
        (id SERIAL PRIMARY KEY NOT NULL,
        title VARCHAR (250) NOT NULL,
        subtitle VARCHAR (250) NOT NULL,
        body TEXT   NOT NULL,
        created_on TIMESTAMP NOT NULL,
        img_url TEXT NOT NULL,
        github_url TEXT)
        '''

    cursor.execute(create_table_query)

def insert_table_data():
    title = "creating blog"
    subtitle = "this is another string"
    body = "this is the body of the blog"
    dt = datetime.now(timezone.utc)
    img_url = r"https://upload.wikimedia.org/wikipedia/commons/8/80/Equus_asinus_Kadzid%C5%82owo_001.jpg"
    query = '''INSERT INTO blog_posts (title, subtitle, body, created_on, img_url)
    VALUES (%s, %s, %s, %s, %s) RETURNING id;'''
    
    cursor.execute(query, (title, subtitle, body, dt, img_url))
    
    


# BASE 
try:
    conn = psycopg2.connect(
        database="my_blog",
        user='postgres',
        password=os.getenv('PSQL_PASSWORD'),
        host='localhost',
        port= '5432'
    )
    
    conn.autocommit = True
    
    # Creating a cursor object
    cursor = conn.cursor()

    # PLACE DESIRED INTERACTION WITH DATABASE BELOW
    insert_table_data()

    # COMMIT CHANGES
    conn.commit()


    # TEST PSQL BY PRINTING DETAILS
    # print("PostgreSQL server information")
    # print(conn.get_dsn_parameters(), "\n")
    # # BY EXERCUTING A SQL QUERY
    # cursor.execute("SELECT version();")
    # # FETCH RESULT
    # record = cursor.fetchone()
    # print("You are connected to - ", record, "\n")

    
    
    # query to create a database 
    # sql = ''' CREATE database my_blog ''';
    
    # executing above query
    # cursor.execute(sql)
    # print("Database has been created successfully !!");
    
except Error as error:
    print("Error while connecting to PSQL", error)

finally: 
    # CLOSE CONNECTION
    cursor.close()
    conn.close()
    print("PSQL connection is closed")


#FUNCTION TO GET RECORDS IN MAIN.PY
def get_records(table_name):
    try:
        conn = psycopg2.connect(
            database="my_blog",
            user='postgres',
            password=os.getenv('PSQL_PASSWORD'),
            host='localhost',
            port= '5432'
        )
        conn.autocommit = True
    
        # Creating a cursor object
        cursor = conn.cursor()

        # PLACE DESIRED INTERACTION WITH DATABASE BELOW
        query = f'''SELECT * FROM {table_name}'''
        cursor.execute(query)
        result = cursor.fetchall()
        return result

        # COMMIT CHANGES
        conn.commit()

    except Error as error:
        print("Error while connecting to PSQL", error)

    finally: 
        # CLOSE CONNECTION
        cursor.close()
        conn.close()
        print("PSQL connection is closed")