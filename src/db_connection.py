import os
import sqlite3
from constants import PRODUCTION, TESTING, DEVELOPMENT


dirname = os.path.dirname(__file__)
env = os.getenv("ENV").lower()
if env not in [PRODUCTION, TESTING, DEVELOPMENT]:
    raise Exception(f"Environment {env} not recognized.")


def _get_db_path():
    db_file = f"database.{env}.sqlite"
    return os.path.join(dirname, "..", "data", db_file)


def _get_script_path() -> str:
    script_file = f"init.{env}.sql"
    return os.path.join(dirname, "..", "scripts", script_file)


connection = sqlite3.connect(_get_db_path())
connection.row_factory = sqlite3.Row
with open(_get_script_path(), "r") as script_file:
    init_script = script_file.read()
connection.cursor().executescript(init_script)


def get_db_connection():
    return connection
