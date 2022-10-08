# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json #by ctzfamioy
import os

ARQ_API_URL = "https://arq.hamker.in"
ARQ_API_KEY =  "KGTHQB-IKDNAI-XXFCND-VDZFQI-ARQ"

def get_user_list(config, key):
    with open('{}/VegetaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 7623447   # integer value, dont use ""
    API_HASH = "e02d7f441208afa97fccf72517c14a10"
    TOKEN = "5608162397:AAEiImofcExh6Du7WmchgpoqPGRzAPFHj4c"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 51897675  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "awesome_gtashxd"
    SUPPORT_CHAT = 'team_wolf_004'  #Your own group for support, do not add the @
    UPDATES_CHANNEL = 'teamwolf_updates' #Your own channel for Updates of bot, Do not add @
    JOIN_LOGGER = - -1767355847  #Prints any new group the bot is added to, prints just the name and ID.
    REM_BG_API_KEY = "dxsh728mZMDmj4ijSZCNPZig"
    EVENT_LOGS = -1806602433  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key -
    SPAMWATCH_SUPPORT_CHAT = "@Team_Wolf_004"
    BOT_ID = "5608162397"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
