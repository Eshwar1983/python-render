import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get URI from Render Environment Variables
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["school_db"]
collection = db["students"]


@app.get("/data")
def get_data():
  documents = list(collection.find({}, {"_id": False}))
  return {"data": documents}
