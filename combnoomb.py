import discord
import os
import pymongo
from pymongo import MongoClient
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
SERVERID = os.getenv('ID')

bot = commands.Bot(command_prefix = '$')

cluster = MongoClient("mongodb+srv://Nikhil0503:<NihiMuga667>@cluster0.souc1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["LinearCombsDiscord"]
collection = db["matricesvectors"]

@bot.event
async def on_ready():
    print(f'{bot.user} is now ready to work!')

@bot.event
async def on_message(message):
    if(message == 'test'):
        print('Hello World')
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    userName = ctx.message.name
    userID = ctx.message.name.id
    collection.insert_one({
        "id": userID, 
        "nameOnDiscord": userName,
        })
    await ctx.reply("Hello!")

@bot.command()
async def createMatrix(ctx, length:int, width:int):
    return None

bot.run(TOKEN)