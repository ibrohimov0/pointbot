from bot.database.mongo import invites, users

def save_invite(owner_id, link):
    invites.insert_one({
        "invite_link": link,
        "ownerTelegramId": owner_id,
        "uses": 0
    })

    users.update_one(
        {"telegramId": owner_id},
        {"$push": {"inviteLinks": {"link": link, "uses": 0}}}
    )

def find_invite_owner(link):
    inv = invites.find_one({"invite_link": link})
    return inv["ownerTelegramId"] if inv else None

def increase_invite_usage(link):
    invites.update_one(
        {"invite_link": link},
        {"$inc": {"uses": 1}}
    )