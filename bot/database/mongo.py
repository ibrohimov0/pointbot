from pymongo import MongoClient
from bot.config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["telegram_bot"]
users = db["users"]
invites = db["invites"]