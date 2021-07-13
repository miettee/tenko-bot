import dotenv
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

db_password = os.getenv("DATABASE_PASSWORD")
