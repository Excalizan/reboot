import discord
from discord.ext import commands
import json


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.last_msg = None

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message

    @commands.command()
    async def snipe(self, ctx: commands.Context):
        if not self.last_msg:
            await ctx.send("There's nothing to snipe!")
            return

        author = self.last_msg.author
        content = self.last_msg.content

        embed = discord.Embed(
            title=f"Message from {author.name}:", description=content)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, type=commands.BucketType.user)
    async def changeprefix(self, ctx, prefix):
        with open('cogs/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('cogs/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: "{prefix}"')

        name = f'{prefix}BotBot'

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Pong!", description=f"My ping is: {round(self.bot.latency * 1000)}ms", color=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx: commands.Context, member: discord.Member = None):
        if member == None:
            if ctx.author.avatar == None:
                await ctx.send(f"The user '{ctx.author.name}' has no profile picture...")

            else:
                embed = discord.Embed(
                    title=f"Profile picture of {ctx.author.name}:")
                embed.set_image(url=ctx.author.avatar)
                await ctx.send(embed=embed)

        elif member != None:
            if member.avatar == None:
                await ctx.send(f"The user '{member.name}' has no profile picture...")
            else:
                embed = discord.Embed(
                    title=f"Profile picture of {member.name}:")
                embed.set_image(url=member.avatar)
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
