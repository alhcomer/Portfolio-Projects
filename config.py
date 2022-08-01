import urllib
import os
from dotenv import load_dotenv

load_dotenv()

psql_password = urllib.parse.quote_plus(os.environ.get("PSQL_PASSWORD"))
database_uri = f"postgresql+psycopg2://postgres:{psql_password}@localhost:5432/my_blog"
