import discord
from discord.ext import commands


class App_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    guild_ids=[855356426600054814]


def setup(bot):
    bot.add_cog(App_Commands(bot))
