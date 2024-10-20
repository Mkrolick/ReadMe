from cmd import IDENTCHARS
import datetime
from email import message
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from sql_methods import *
import time

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
print(token)


intents = discord.Intents.all()

client = discord.Client(intents=intents)

# log in user to client
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(token)