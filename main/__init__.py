#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("22783302", default=None, cast=int)
API_HASH = config("d2d9ed1561e4e8c8ab2d99d10742ba3d", default=None)
BOT_TOKEN = config("6194231915:AAHrfdvFtZPZFr6prYctAtkD6t1wEbySpKw", default=None)
SESSION = config("BQBapoFKC0yDITGFc1WDI_MCPJfiENi868uQQV92Uce3Chv7MM2vLmUPQ0Ysb4U33COQuuX-RnF1Fe2rhYGMEBOfN5zdxP9nxTlsHW7rQxsuQDFidWqS7WCk0kuAeZO9iFUvqpAcp1oU3EytBEdS8binLjiceYtrCj_Lrf8XmY-i1OhxbC_CvP71wt1EyNydoyz4yQH7_iGuGHQj3AzLRmhwZFz6OS2QFVZ1QrbeMAaefW_vhw-HTeIAPD2mlC-_dEO6z8nwUVcEQUBYwcqnNlF05FvGPZMuII9RERCMmNJKUErOoBFk3ZMYoirKRQ96WVUqm0nRktQjKI9RVOwI74Zlc-G4OAA", default=None)
FORCESUB = config("-1001613168852", default=None)
AUTH = config("1944172600", default=None, cast=int)

bot = TelegramClient(bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
