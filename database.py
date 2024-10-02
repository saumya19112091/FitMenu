from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy import text
import os

load_dotenv(".env")

# Example connection string for PostgreSQL
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Create an engine that connects to the database
engine = create_engine(DATABASE_URL)

# Test the connection
with engine.connect() as connection:
    print("Connection successful!")


with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM grocery_items_new"))


    print(result.fetchall())
