from xmlrpc.client import DateTime
from dotenv import load_dotenv
from sqlalchemy import Integer, table
from sqlalchemy import create_engine, Table, Column, String, MetaData, DateTime
import urllib.parse
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from config import psql_password, database_uri

load_dotenv()

Base = declarative_base()

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    img_url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    subtitle = Column(String, nullable=False)
    body = Column(String, nullable=False)
    published = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return "<Blogs(img_url={}, title='{}', subtitle='{}', body='{}', published={})>"\
            .format(self.img_url, self.title, self.subtitle, self.body, self.published)

class Portfolio(Base):
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True)
    img_url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    subtitle = Column(String, nullable=False)
    body = Column(String, nullable=False)
    published = Column(DateTime(timezone=True), server_default=func.now())
    github_url = Column(String, nullable=False)


engine = create_engine(database_uri)
Base.metadata.create_all(engine)