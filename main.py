from msilib.schema import Error
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2
from dotenv import load_dotenv
from psycopg2 import sql, Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

load_dotenv()

# INITIALISE APPLICATION
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY')

# CREATE DATABASE IF ONE DOES NOT EXIST
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
    create_table_query = '''CREATE TABLE [IF NOT EXISTS] blog_posts 
        (id SERIAL PRIMARY KEY NOT NULL,
        title VARCHAR (250) NOT NULL,
        subtitle VARCHAR (250) NOT NULL,
        body TEXT   NOT NULL,
        created_on TIMESTAMP NOT NULL)
        '''

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

# CONFIGUE ROUTING FOR PAGES
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/blog-post/<int:post_id>')
# def show_post(post_id):
#     requested_post = BlogPost.query.get(post_id)
#     if request.method == 'GET':
#         pass
        

# # RUN COMMAND
# if __name__ == '__main__':
#     app.run(debug=True)