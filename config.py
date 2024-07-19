from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("28298365", 6))
    API_HASH = getenv("9647ab7fc03a8a93f701a5528b2f206e", None)
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    STRING_SESSION = getenv("STRING_SESSION", None)
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", None)
    OWNER_ID = int(getenv("OWNER_ID", "5536168611"))  # sᴛᴀʀᴛ @Exon_Robot ᴛʏᴘᴇ /id
    OWNER_USERNAME = getenv("OWNER_USERNAME", "DARKCURSED0")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "beta_support")
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002239117016"))
    MONGO_URI = getenv("MONGO_DB_URI")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL")

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
