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
    return render_template(
        'index.html',
        blog_records=blog_records, portfolio_records=portfolio_records
        )

@app.route('/blog-post/<int:post_id>')
def show_blog(post_id):
    blog_records = psql.get_records("blog_posts")
    blog_post = None
    for blog in blog_records:
        if blog[0] == post_id:
            blog_post = blog
    return render_template('blog-post.html', blog_post=blog_post)

@app.route('/portfolio-post/<int:post_id>')
def show_portfolio(post_id):
    portfolio_records = psql.get_records("portfolio_posts")
    portfolio_post = None
    for record in portfolio_records:
        if record[0] == post_id:
            portfolio_post = record
    return render_template('portfolio-post.html', portfolio_post=portfolio_post)


# NEED TO ADD CONTACT FORM FUNCTIONALITY
@app.route('/process_email', methods=['POST'])
def process_email():
    pass

# RUN COMMAND
if __name__ == '__main__':
    app.run(debug=True)
