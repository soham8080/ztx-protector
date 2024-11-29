class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5595153270"
    sudo_users = "6257270528", "6321134824", "5595153270"
    GROUP_ID = -1002126989582
    TOKEN = "7167198617:AAHHj3-eWVB-JOpVXn7ZKhchEvumYKJiVdg"
    mongo_url = "mongodb+srv://ztx:ztxwaifu@cluster0.dpny5vq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/62531cee34e5c9f6599b4.jpg"]
    SUPPORT_CHAT = "Ɓ ʟ ᴀ ᴅ ᴇ メ ƈ ᴏ ᴍ ᴍ ᴜ ɴ ɪ ᴛ ʏ"
    UPDATE_CHAT = "Nᴀʀᴜᴛᴏ Uᴘᴅᴀᴛᴇs"
    BOT_USERNAME = "Seal_Your_Waifu_Bot"
    CHARA_CHANNEL_ID = "-1002126989582"
    api_id = 22792918
    api_hash = "ff10095d2bb96d43d6eb7a7d9fc85f81"
    
    STRICT_GBAN = True
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
