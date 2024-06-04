import pymongo
from dotenv import load_dotenv
from discord.ext import commands
import os
import discord

#Variables and configuration
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = discord.Bot(intents=intents)
try:
    testing = os.environ["TESTING"]
except:
    testing = "false"
try:
    testing_token = os.environ["TESTING_TOKEN"]
except:
    print("Testing token was not set.")
try:
    mongo_string = os.environ["MONGO_STRING"]
except:
    mongo_string = None


#Database Setup
if testing == "false":
   if mongo_string == None:
    username = os.environ["MONGO_USER"]
    password = os.environ["MONGO_PASS"]
    mongo = pymongo.MongoClient(f"mongodb://{username}:{password}@mongodb/")
   else:
    mongo = pymongo.MongoClient(os.environ["MONGO_STRING"])
    db = mongo.float
elif testing == "true":
    mongo = pymongo.MongoClient(os.environ["MONGO_TESTING"])
    db = mongo.float_testing
