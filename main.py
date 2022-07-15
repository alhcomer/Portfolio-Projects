from msilib.schema import Error
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2
from dotenv import load_dotenv
from psql import get_records

load_dotenv()

# INITIALISE APPLICATION
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY')


# CONFIGUE ROUTING FOR PAGES
@app.route('/')
def home():
    blog_records = get_records("blog_posts")
    portfolio_records = get_records("portfolio_posts")
    return render_template('index.html', blog_records=blog_records, portfolio_records=portfolio_records)

@app.route('/blog-post/<int:post_id>')
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    if request.method == 'GET':
        pass
        

# RUN COMMAND
if __name__ == '__main__':
    app.run(debug=True)