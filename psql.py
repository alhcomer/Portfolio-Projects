from psycopg2 import sql, Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import table

load_dotenv()

# CREATE DATABASE IF ONE DOES NOT EXIST

def insert_table_data(table_name):
    if table_name == "blog_posts":
        pass

    if table_name == "portfolio_posts":
        pass

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

    # SQL query to create blog table
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
    conn.commit()

    print("Table created successfully in PSQL")

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
    
    # Closing the connection
    # conn.close()

except [Exception, Error] as error:
    print("Error while connecting to PSQL", error)

finally: 
    cursor.close()
    conn.close()
    print("PSQL connection is closed")