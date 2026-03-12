from pymongo import MongoClient
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
import certifi

# Load environment variables
load_dotenv()

USERNAME = quote_plus(os.getenv("MONGO_USER"))
PASSWORD = quote_plus(os.getenv("MONGO_PASSWORD"))
DB_NAME = os.getenv("MONGO_DB")
CLUSTER = os.getenv("MONGO_CLUSTER")

MONGO_URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@{CLUSTER}/{DB_NAME}?retryWrites=true&w=majority"

# Use certifi to verify SSL certificates
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())

db = client[DB_NAME]