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


bot = commands.Bot(command_prefix='>', intents=intents)

# simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


# gives server info
@bot.command()
async def server_info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Server Details", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
    await ctx.send(embed=embed)


@bot.command()
async def hunt(ctx):
    print("Hunt command started")
    channels = ctx.guild.channels
    channels = [channel for channel in channels if channel.type == discord.ChannelType.text]
    
    for channel in channels:
        
        messages = [message async for message in channel.history(limit=10000)]
        #print("BRUH")
        #print(messages[0].content.encode('utf8'))

        with open("messages.csv", "a") as f:
            for message in messages:
                try:
                    f.write(f"{message.author.name},{message.content.encode('utf8')},{message.created_at}\n")
                except:
                    pass
            print("Working?")
    print("Ran")
    

    

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    




bot.run(token)
