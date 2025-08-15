import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")

MONGO_HOST = os.environ.get("MONGO_HOST", "mongo")
MONGO_PORT = int(os.environ.get("MONGO_PORT", "27017"))
MONGO_USERNAME = os.environ.get("MONGO_INITDB_ROOT_USERNAME", "root")
MONGO_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD", "secret")
MONGO_DB = os.environ.get("MONGO_DB", "test")

mongo_uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"

mongo_client = MongoClient(mongo_uri)

def insert_test_document():
  db = mongo_client[MONGO_DB]
  test_collection = db.test_collection
  res = test_collection.insert_one({"name": "JJNi", "student": True})
  print(res)

# Example usage:
# collection = db["your_collection"]
# result = collection.find_one({})
