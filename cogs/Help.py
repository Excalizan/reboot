import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(
            title="Help",
            description="Use !help <command> for extended information on a command \n**[parameter]** = required \n**<parameter>** = optional",
            color=ctx.author.color)

        em.add_field(name="Help", value="help", inline=False)
        em.add_field(name="General",
                     value="ping, changeprefix, avatar, snipe",
                     inline=False)
        em.add_field(name="Moderation",
                     value="kick, ban, mute, unmute, clear, timeout",
                     inline=False)
        em.add_field(name="Level",
                     value="level",
                     inline=False)
        await ctx.send(embed=em)

    @help.command()
    async def ping(self, ctx):
        em = discord.Embed(title="Ping",
                           description="Shows ping of the bot",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!ping")
        await ctx.send(embed=em)

    @help.command()
    async def changeprefix(self, ctx):
        em = discord.Embed(title="Change Prefix",
                           description="Changes the prefix of the bot",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!changeprefix [new_prefix]")
        em.add_field(name="**Cooldown**", value="Usable once every 10 seconds")
        await ctx.send(embed=em)

    @help.command()
    async def avatar(self, ctx):
        em = discord.Embed(title="Avatar",
                           description="Send the avatar to the provided user\n If no user is provided, the bot will send the author's avatar",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!avatar <member>")
        await ctx.send(embed=em)

    @help.command()
    async def snipe(self, ctx):
        em = discord.Embed(title="Snipe",
                           description="Snipe the last deleted message",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!snipe")
        await ctx.send(embed=em)


    @help.command()
    async def kick(self, ctx):
        em = discord.Embed(title="Kick",
                           description="Kicks the given user from the guild",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!kick [user] <reason>")
        await ctx.send(embed=em)

    @help.command()
    async def ban(self, ctx):
        em = discord.Embed(title="Ban",
                           description="Bans the given user from the guild",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!ban [user] <reason>")
        await ctx.send(embed=em)

    @help.command()
    async def mute(self, ctx):
        em = discord.Embed(title="Mute",
                           description="Mutes the user until you unmute them",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!mute [user] <reason>")
        await ctx.send(embed=em)

    @help.command()
    async def unmute(self, ctx):
        em = discord.Embed(title="Unmute",
                           description="Unmutes the muted user",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!unmute [user]")
        await ctx.send(embed=em)

    @help.command()
    async def clear(self, ctx):
        em = discord.Embed(title="Clear",
                           description="Delete messages from the text channel with the given amount",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!clear <amount>")
        em.add_field(name="**Aliases**", value="purge, delete")
        await ctx.send(embed=em)

    @help.command()
    async def purge(self, ctx):
        em = discord.Embed(title="Purge",
                           description="Delete messages from the text channel with the given amount",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!purge <amount>")
        em.add_field(name="**Aliases**", value="clear, delete")
        await ctx.send(embed=em)

    @help.command()
    async def delete(self, ctx):
        em = discord.Embed(title="Delete",
                           description="Delete messages from the text channel with the given amount",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!delete <amount>")
        em.add_field(name="**Aliases**", value="clear, purge")
        await ctx.send(embed=em)
    
    @help.command()
    async def timeout(self, ctx):
        em = discord.Embed(title="Timeout",
                           description="Timeout the given user for the given amount of time",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!timeout [user] <amount>")
        await ctx.send(embed=em)

    @help.command()
    async def level(self, ctx):
        em = discord.Embed(title="Level",
                           description="See your level information",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!level [user] <reason>")
        em.add_field(name="**Aliases**", value="rank, lvl")
        await ctx.send(embed=em)

    @help.command()
    async def rank(self, ctx):
        em = discord.Embed(title="Level",
                           description="See your level information",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!rank [user] <reason>")
        em.add_field(name="**Aliases**", value="level, lvl")
        await ctx.send(embed=em)

    @help.command()
    async def lvl(self, ctx):
        em = discord.Embed(title="Level",
                           description="See your level information",
                           color=ctx.author.color)

        em.add_field(name="**Syntax**", value="!lvl [user] <reason>")
        em.add_field(name="**Aliases**", value="rank, level")
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Help(bot))
