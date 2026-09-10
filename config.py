import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


def _int(name, default=0):
    val = getenv(name)
    if val is None or str(val).strip() == "":
        return default
    try:
        return int(str(val).strip())
    except (TypeError, ValueError):
        return default


def _str(name, default=""):
    val = getenv(name)
    if val is None:
        return default
    return str(val).strip()


# --------------------- Telegram ---------------------
API_ID = _int("API_ID", 0)
API_HASH = _str("API_HASH", "")
BOT_TOKEN = _str("BOT_TOKEN", "")

OWNER_USERNAME = _str("OWNER_USERNAME", "")
BOT_USERNAME = _str("BOT_USERNAME", "")
BOT_NAME = _str("BOT_NAME", "NISHAD MUSIC")
ASSUSERNAME = _str("ASSUSERNAME", "")

# --------------------- Music API ---------------------
BASE_URL = _str("BASE_URL", "https://babyapi.pro")
API_KEY = _str("API_KEY", "")

# --------------------- Mongo (no hardcoded password) ---------------------
MONGO_DB_URI = _str("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = _int("DURATION_LIMIT", 17000)
LOGGER_ID = _int("LOGGER_ID", 0)
OWNER_ID = _int("OWNER_ID", 0)

HEROKU_APP_NAME = _str("HEROKU_APP_NAME", "")
HEROKU_API_KEY = _str("HEROKU_API_KEY", "")
UPSTREAM_REPO = _str(
    "UPSTREAM_REPO",
    "https://github.com/Kartiknishad36/NISHAD40",
)
UPSTREAM_BRANCH = _str("UPSTREAM_BRANCH", "main")
GIT_TOKEN = _str("GIT_TOKEN", "")

SUPPORT_CHANNEL = _str("SUPPORT_CHANNEL", "https://t.me/YourChannel")
SUPPORT_CHAT = _str("SUPPORT_CHAT", "https://t.me/YourSupport")
SOURCE = _str("SOURCE", "https://github.com/Kartiknishad36/NISHAD40")
CHAT = _str("CHAT", "https://t.me/YourSupport")

AUTO_LEAVING_ASSISTANT = _str("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = _int("ASSISTANT_LEAVE_TIME", 9000)
SONG_DOWNLOAD_DURATION = _int("SONG_DOWNLOAD_DURATION", 9999999)
SONG_DOWNLOAD_DURATION_LIMIT = _int("SONG_DOWNLOAD_DURATION_LIMIT", 9999999)

SPOTIFY_CLIENT_ID = _str("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = _str("SPOTIFY_CLIENT_SECRET", "")
PLAYLIST_FETCH_LIMIT = _int("PLAYLIST_FETCH_LIMIT", 25)

TG_AUDIO_FILESIZE_LIMIT = _int("TG_AUDIO_FILESIZE_LIMIT", 5242880000)
TG_VIDEO_FILESIZE_LIMIT = _int("TG_VIDEO_FILESIZE_LIMIT", 5242880000)

# Assistant session (Railway: STRING_SESSION)
STRING1 = _str("STRING_SESSION", "") or _str("STRING1", "")
STRING2 = _str("STRING2", "")
STRING3 = _str("STRING3", "")
STRING4 = _str("STRING4", "")
STRING5 = _str("STRING5", "")

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = _str(
    "START_IMG_URL",
    "https://raw.githubusercontent.com/BABY-MUSIC/SPOTIFY_MUSIC/main/BABYMUSIC/assets/assets/public.jpg",
)
PING_IMG_URL = _str(
    "PING_IMG_URL",
    "https://telegra.ph/file/fd827f9a4fe8eaa3e8bf4.jpg",
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/c832e84cd991c865c7e4f.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
IQ_Proxy = "https://i.ytimg.com/vi"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] SUPPORT_CHANNEL must start with https://"
    )

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] SUPPORT_CHAT must start with https://"
    )

__all__ = ["IQ_Proxy"]
