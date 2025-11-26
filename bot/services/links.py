from bot.database.mongo import links

def get_links(): 
    return links.find()

