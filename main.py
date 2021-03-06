from flask import Flask, render_template, url_for, request
import os
from dotenv import load_dotenv
from crud import get_blog_posts, get_portfolio_posts
from forms import ContactForm
import pandas as pd
from flask_wtf.csrf import CSRFProtect
from blog_requests import get_contribution_count

load_dotenv()

# Initialise Application
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("APP_SECRET_KEY")
csrf = CSRFProtect(app)
csrf.init_app(app)

# Configure Routing for Pages
@app.route("/", methods=["GET", "POST"])
def home():
    contact_form = ContactForm()
    blog_records = get_blog_posts()
    portfolio_records = get_portfolio_posts()
    github_contributions = get_contribution_count()

    if request.method == "POST" and contact_form.validate_on_submit():
        # check if above request.method == post is necessary
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        body = request.form["body"]
        res = pd.DataFrame(
            {"name": name, "email": email, "subject": subject, "body": body}, index=[0]
        )
        res.to_csv("./contactmeMessage")

    return render_template(
        "index.html",
        blog_records=blog_records,
        portfolio_records=portfolio_records,
        contact_form=contact_form,
        github_contributions=github_contributions
    )

@app.route("/blog-post/<int:post_id>")
def show_blog(post_id):
    blog_records = get_blog_posts()
    for blog in blog_records:
        if blog.id == post_id:
            blog_post = blog
    return render_template("blog-post.html", blog_post=blog_post)


@app.route("/portfolio-post/<int:post_id>")
def show_portfolio(post_id):
    portfolio_records = get_portfolio_posts()
    for record in portfolio_records:
        if record.id == post_id:
            portfolio_post = record
    return render_template("portfolio-post.html", portfolio_post=portfolio_post)

# Run Application
if __name__ == "__main__":
    app.run(debug=True)
