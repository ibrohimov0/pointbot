from bot.database.mongo import users

def get_user(tg_id):
    return users.find_one({"telegramId": tg_id})

def create_user(tg_id, username):
    users.insert_one({
        "telegramId": tg_id,
        "username": username,
        "points": 0,
        "firstPoint": False
    })

def add_first_point(tg_id):
    users.update_one(
        {"telegramId": tg_id},
        {"$set":{"firstPoint": True}}
    )

def add_point(tg_id):
    users.update_one(
        {"telegramId": tg_id},
        {"$inc": {"points": 1}}
    )