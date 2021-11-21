import os
import sqlite3
from constants import PRODUCTION, TESTING, DEVELOPMENT


dirname = os.path.dirname(__file__)
env = os.getenv("ENV").lower()
if env not in [PRODUCTION, TESTING, DEVELOPMENT]:
    raise Exception(f"Environment {env} not recognized.")

db_file = f"database.{env}.sqlite"
connection = sqlite3.connect(os.path.join(dirname, "..", "data", db_file))
connection.row_factory = sqlite3.Row


def get_db_connection():
    return connection
