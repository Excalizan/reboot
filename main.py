import discord
from discord.ext import commands
import os
from os import listdir
from dotenv import load_dotenv
import json
import asyncio

# load the .env file and get the token
load_dotenv()
TOKEN = os.getenv("TOKEN")


# get the prefix for the given guild
def get_prefix(bot, message):
    with open("cogs/prefixes.json", "r") as f:
        prefixes = json.load(f)
        if not str(message.guild.id) in prefixes:
            prefixes[str(message.guild.id)] = "!"

            with open(
                "cogs/prefixes.json", "w"
            ) as f:
                json.dump(prefixes, f, indent=4)
    return prefixes[str(message.guild.id)]


# initialize the bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=(get_prefix), intents=intents)
bot.remove_command("help")


# setup the on_ready event
@bot.event
async def on_ready():
    print(f"Your bot {bot.user} is ready!")
    await bot.change_presence(
        activity=discord.Game(name=f"in {len(bot.guilds)} servers")
    )


# load the cogs
for filename in listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


# !run the bot
bot.wait_until_ready()
bot.run(TOKEN)
