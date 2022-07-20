from msilib.schema import Error
from flask import Flask, render_template, url_for, request
import os
from dotenv import load_dotenv
from psql import PostgresManager

load_dotenv()

# INITIALISE APPLICATION
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY')
psql = PostgresManager()

# CONFIGUE ROUTING FOR PAGES
@app.route('/')
def home():
    blog_records = psql.get_records("blog_posts")
    portfolio_records = psql.get_records("portfolio_posts")
    print(portfolio_records)
    return render_template('index.html', blog_records=blog_records, portfolio_records=portfolio_records)

@app.route('/blog-post/<int:post_id>')
def show_post(post_id):
    pass
    # requested_post = BlogPost.query.get(post_id)
    # if request.method == 'GET':
    #     pass


# RUN COMMAND
if __name__ == '__main__':
    app.run(debug=True)