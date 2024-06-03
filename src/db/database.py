import os

from pymongo import MongoClient

# Replace with your MongoDB URI
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["forecast_db"]
forecast_collection = db["forecasts"]
