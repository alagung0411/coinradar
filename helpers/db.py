from pymongo import MongoClient
import os

# print(os.environ['MONGODB_URI'])
# MONGODB_URI = "mongodb+srv://kamansyah038:kaman@cluster0.bf58n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGODB_URI = os.environ["MONGODB_URI"]
DB_NAME = os.environ["DB_NAME"]
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]