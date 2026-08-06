import os
from flask import Flask  # or FastAPI, Streamlit, Dash, etc.
from pymongo import MongoClient

app = Flask(__name__)

# 1. Fetching user-defined environment variables from Render
DATABASE_URL = os.environ.get("DATABASE_URL")
client = MongoClient(DATABASE_URL)
db = client["school_db"]
collection = db["students"]
API_SECRET = os.environ.get("API_KEY")

# 2. Binding your host and port dynamically (Crucial for web hosting)
# Render automatically injects a dynamic PORT variable at runtime.
HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 10000))

@app.get("/api")
def get_data():
  documents = list(collection.find({}, {"_id": False}))
  return {"api": documents}

if __name__ == "__main__":
    # Ensure your app binds to 0.0.0.0 and the assigned port
    app.run(host=HOST, port=PORT)
