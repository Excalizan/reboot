import discord
from discord.ext import commands
import json


class Event_Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("cogs/prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = "!"

        with open("cogs/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

        channel = guild.system_channel
        embed = discord.Embed(
            title="Thanks for inviting me!",
            description=f"Hello {guild.name}, thanks for adding me to your server!",
            color=discord.Colour.green(),
        )
        embed.add_field(
            name="How to start?",
            value="You can start using me by typing '!help' in any text channel I have permission to speak!",
            inline=True,
        )
        if channel and channel.permissions_for(guild.me).send_messages:
            await channel.send(embed=embed)
        elif not channel:
            await guild.owner.send(embed=embed)
        await self.bot.change_presence(
            activity=discord.Game(name=f"in {len(self.bot.guilds)} servers")
        )

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("cogs/prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open("cogs/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        await self.bot.change_presence(
            activity=discord.Game(name=f"in {len(self.bot.guilds)} servers")
        )

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if not self.bot.guild.id == 110373943822540800:
            channel = member.guild.system_channel
            if channel is not None:
                await channel.send(f"Welcome to the server {member.mention}!")



def setup(bot):
    bot.add_cog(Event_Listeners(bot))
