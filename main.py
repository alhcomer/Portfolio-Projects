from msilib.schema import Error
from flask import Flask, render_template, url_for, request
import os
from dotenv import load_dotenv
from crud import get_blog_posts, get_portfolio_posts
from forms import ContactForm

load_dotenv()

# INITIALISE APPLICATION
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY')

# CONFIGUE ROUTING FOR PAGES
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        blog_records = get_blog_posts()
        portfolio_records = get_portfolio_posts()
        contact_form = ContactForm()
        return render_template(
            'index.html',
            blog_records=blog_records, portfolio_records=portfolio_records,
            contact_form=contact_form
            )
    elif request.method == 'POST':
        return 'Form posted.'

@app.route('/blog-post/<int:post_id>')
def show_blog(post_id):
    blog_records = get_blog_posts()
    for blog in blog_records:
        if blog.id == post_id:
            blog_post = blog
    return render_template('blog-post.html', blog_post=blog_post)

@app.route('/portfolio-post/<int:post_id>')
def show_portfolio(post_id):
    portfolio_records = get_portfolio_posts()
    for record in portfolio_records:
        if record.id == post_id:
            portfolio_post = record
    return render_template('portfolio-post.html', portfolio_post=portfolio_post)

if __name__ == '__main__':
    app.run(debug=True)
