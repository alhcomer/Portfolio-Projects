from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import database_uri
from models import Base, Blog
from datetime import datetime

def recreate_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

engine = create_engine(database_uri)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

blog = Blog(
    img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Donkey_in_Clovelly%2C_North_Devon%2C_England.jpg/640px-Donkey_in_Clovelly%2C_North_Devon%2C_England.jpg',
    title = 'How to create your first blog',
    subtitle = 'It can be a real pain',
    body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
)

recreate_db()
s = Session()
s.add(blog)
s.commit()
s.close()