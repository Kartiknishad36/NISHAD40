from pyrogram import Client

from BABYMUSIC.core.bot import BABY
from BABYMUSIC.core.dir import dirr
from BABYMUSIC.core.git import git
from BABYMUSIC.core.userbot import Userbot
from BABYMUSIC.misc import dbb, heroku
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = BABY()
userbot = Userbot()

# Safone optional — missing package pe bot crash na ho
try:
    from SafoneAPI import SafoneAPI

    api = SafoneAPI()
    LOGGER(__name__).info("SafoneAPI loaded.")
except Exception as e:
    api = None
    LOGGER(__name__).warning(f"SafoneAPI disabled: {e}")

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
