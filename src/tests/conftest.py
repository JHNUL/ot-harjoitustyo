from game.utils import ImageLoader
from init_db import initialize_db

print("Initializing database for test run")
initialize_db()
ImageLoader.init()
