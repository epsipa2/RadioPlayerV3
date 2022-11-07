"""
RadioPlayerV3, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""


import os
import re
import sys
import heroku3
import subprocess
from dotenv import load_dotenv
try:
    from yt_dlp import YoutubeDL
except ModuleNotFoundError:
    file=os.path.abspath("requirements.txt")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file, '--upgrade'])
    os.execl(sys.executable, sys.executable, *sys.argv)

load_dotenv()

ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://www.liveradio.ie/stations/star-radio-tamil")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM



class Config:

    # Mendatory Variables
    ADMIN = os.environ.get("AUTH_USERS", "")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    ADMINS.append(1316963576)
    API_ID = int(os.environ.get("API_ID", "10670890"))
    API_HASH = os.environ.get("API_HASH", "b8c18624a9a4b397e9989c30904de9d2")
    CHAT_ID = int(os.environ.get("CHAT_ID", " -1001748703009"))
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5541244134:AAEkydEKmFTKGkrQ3KbdPKSsACpCKOpQlLg")
    SESSION = os.environ.get("SESSION_STRING", "BACi0yoAD0GzbOKrkEDUSW_bRWIeCm7wktbj_kICKNwqEM-Hngas8jLXOv_P1-wR7_lllqAFE6jJAuXYE_zsfo8zh68_eTBdGzBO_POxU48ZTeYthe3KeFz5l7h9-8mRLsoTpYOB1Ovb5dA9ddz0c_slXtoVrRGAfkPb80Kynvb28llp4LoePexzOQD9VlROEGwolq3D7s2b8rzpMH8IZxGj33-LXVX3P9ekvqHgC6WE48JN0z6uRP5vDVbsrkFicPa0A6Bt2Tu0y0aJ9VXhY3AmbhPIB7MzfDUMUhFp-zhol-eAdvdgkzAz6KeSaBmD-aBIBUu44wQZLTpQUvP602MqUjJ2EwAAAAB1bUfuAA")

    # Optional Variables
    STREAM_URL=finalurl
    LOG_GROUP=os.environ.get("LOG_GROUP", "")
    LOG_GROUP = int(LOG_GROUP) if LOG_GROUP else None
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "False")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    REPLY_MESSAGE = REPLY_MESSAGE or None
    DELAY = int(os.environ.get("DELAY", 10))
    EDIT_TITLE=os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "False":
        EDIT_TITLE=None
    RADIO_TITLE=os.environ.get("RADIO_TITLE", "RADIO 24/7 | LIVE")
    if RADIO_TITLE == "False":
        RADIO_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 15000))

    # Extra Variables ( For Heroku )
    API_KEY = os.environ.get("fe516070-0270-48af-96a4-d2fbc01832bf", None)
    APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    if not API_KEY or \
       not APP_NAME:
       HEROKU_APP=None
    else:
       HEROKU_APP=heroku3.from_key(API_KEY).apps()[APP_NAME]

    # Temp DB Variables ( Don't Touch )
    msg = {}
    playlist=[]

