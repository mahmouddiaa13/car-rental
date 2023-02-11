import os
from dotenv import load_dotenv

load_dotenv()
# Mysql
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DATABASE_NAME = os.getenv("MYSQL_DATABASE_NAME")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
