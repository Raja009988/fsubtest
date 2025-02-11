# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

APP_ID = int(os.getenv("APP_ID", "28653571"))

API_HASH = os.getenv("API_HASH", "eca35c0338b15aa33cc2d5df4a5a7b65")

CHANNEL_DB = int(os.getenv("CHANNEL_DB", ""))
OWNER = os.getenv("OWNER", "akwcuy")
PROTECT_CONTENT = strtobool(os.getenv("PROTECT_CONTENT", "True"))

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", None)

UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "master")

# Database type
DATABASE_TYPE = os.getenv("DATABASE_TYPE", "")

# Database
DB_URL = os.getenv("DB_URL", "")

# Database Name MongoDB
DB_NAME = os.getenv("DB_NAME", "")


FORCE_SUB_ = {}
FSUB_TOTAL = 1
while True:
    key = f"FORCE_SUB_{FSUB_TOTAL}"
    value = os.getenv(key)
    if value is None:
        break
    FORCE_SUB_[FSUB_TOTAL] = int(value)
    FSUB_TOTAL += 1

BUTTON_ROW = int(os.getenv("BUTTON_ROW", 3))

BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))

START_MSG = os.getenv(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>SMUMPUNG LAGI PROMO LIST GROUB PRIVAT VIP ASUPAN TANPA LINK/BOT https://t.me/ROOMVIIPKU/10\n\n>VIP RANDOM 50K\n>VIP OME TV 35K\n>VIP BOCHIEL 50K\n>VIP HIJAB 35K\n>VIP LIVE RECORD 35K\n\n❏ PAYMENT\n├• DANA\n├• GOPAY\n\nMINAT JOIN? LANGSUNG HUB\n╰►@etminvvipku</b>",
)
try:
    ADMINS = [int(x) for x in (os.getenv("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

FORCE_MSG = os.getenv(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nMUMPUNG LAGI PROMO LIST GROUB PRIVAT VIP ASUPAN TANPA LINK/BOT https://t.me/ROOMVIIPKU/10\n\n>VIP RANDOM 50K\n>VIP OME TV 35K\n>VIP BOCHIEL 50K\n>VIP HIJAB 35K\n>VIP LIVE RECORD 35K\n\n❏ PAYMENT\n├• DANA\n├• GOPAY\n\nMINAT JOIN? LANGSUNG HUB\n╰►@etminvvipku</b>",
)


CUSTOM_CAPTION = os.getenv("CUSTOM_CAPTION", None)


DISABLE_CHANNEL_BUTTON = strtobool(os.getenv("DISABLE_CHANNEL_BUTTON", "False"))

ADMINS.extend((1506027871))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
