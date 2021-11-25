import os
from db_connection import get_db_connection


def _get_script_path() -> str:
    env = os.getenv("ENV").lower()
    dirname = os.path.dirname(__file__)
    script_file = f"init.{env}.sql"
    return os.path.join(dirname, "..", "scripts", script_file)


def initialize_db():
    connection = get_db_connection()
    with open(_get_script_path(), "r", encoding="utf8") as script_file:
        init_script = script_file.read()
    connection.cursor().executescript(init_script)
    connection.commit()
