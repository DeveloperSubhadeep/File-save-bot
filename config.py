from os import environ 

class Config:
    API_ID = environ.get("API_ID", "27972068")
    API_HASH = environ.get("API_HASH", "6e7e2f5cdddba536b8e603b3155223c1)
    BOT_TOKEN = environ.get("BOT_TOKEN", "7103264571:AAH71efUXDBlwIpC7OVZNVlZSErYIWuyBrE") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://marge:marge@cluster0.33khk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6075512585').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
