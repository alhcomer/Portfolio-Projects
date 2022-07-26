from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import database_uri
from models import Base, Blog, Portfolio
from datetime import datetime

def recreate_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

engine = create_engine(database_uri)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def create_blog_post():
    blog = Blog(
    img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Donkey_in_Clovelly%2C_North_Devon%2C_England.jpg/640px-Donkey_in_Clovelly%2C_North_Devon%2C_England.jpg',
    title = 'How to create your first blog',
    subtitle = 'It can be a real pain',
    body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    s = Session()
    s.add(blog)
    s.commit()
    s.close()

def create_portfolio_post():
    portfolio = Portfolio(
    img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Donkey_in_Clovelly%2C_North_Devon%2C_England.jpg/640px-Donkey_in_Clovelly%2C_North_Devon%2C_England.jpg',
    title = 'This Website!',
    subtitle = 'Created using Flask and SQLAlchemy.',
    body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    github_url = "https://github.com/alhcomer")
    s = Session()
    s.add(portfolio)
    s.commit()
    s.close()

def get_blog_posts():
    s = Session()
    blog_posts = s.query(Blog).all()
    s.close()
    return blog_posts

def get_portfolio_posts():
    s = Session()
    blog_posts = s.query(Portfolio).all()
    s.close()
    return blog_posts


