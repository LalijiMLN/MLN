
import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()




id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


      
# Owner Information
API_ID = int(environ.get("API_ID", "25848289"))
API_HASH = environ.get("API_HASH", "88cf2c17c7a2bd21f4204c89c648dd40")
ADMINS = int(environ.get("ADMINS", "1557042262"))

# Database Information
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://RAS_TEAM:rasteam@123@cluster0.619qk8h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CDB_NAME = environ.get("CDB_NAME", "clonevjbotz")
DB_URI = environ.get("DB_URI", "mongodb+srv://yadavrahul2003:IbRdr2y3Qs5juADm@cluster0.8epud6d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "vjbotz")


# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "7170848508:AAH9Z2rll7vrR_h1huyXs5koALxhTb7SexE")
BOT_USERNAME = environ.get("BOT_USERNAME", "RAS_Store_Bot") # your bot username without @
PICS = (environ.get('PICS', 'https://graph.org/file/53532b4697b852c3d8fd2.jpg https://graph.org/file/53532b4697b852c3d8fd2.jpg')).split() # Bot Start Picture

# Auto Delete Information
AUTO_DELETE = int(environ.get("AUTO_DELETE", "10")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "600")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001923834324"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002128363054')).split()]

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)



# File Stream Config
class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'filetolinkvjbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '3'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002141038542'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://ras-avatar.onrender.com"
    else:
        URL = "https://ras-avatar.onrender.com"




    
