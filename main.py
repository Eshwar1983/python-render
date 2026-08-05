import os
from fastapi import FastAPI
from pymongo import MongoClient
from flask_cors import CORS

app = FastAPI()
CORS(app)

# Get URI from Render Environment Variables
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["school_db"]
collection = db["students"]


@app.get("/data")
def get_data():
  documents = list(collection.find({}, {"_id": False}))
  return {"data": documents}
