import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5819824799:AAHzJoDiqDzniXtNpNDo3emgj2GiPJnVefE

")

    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 5166878))
    API_HASH = os.environ.get("fdafb41f9a67f40e34a6c67f47730a92")
    # Get these values from my.telegram.org

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://tron:tron@cluster0.xs0gvih.mongodb.net/?retryWrites=true&w=majority")

