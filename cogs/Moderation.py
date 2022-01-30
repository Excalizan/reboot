import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"User {member.mention} has been kicked. Reason: {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"User {member.mention} has been banned. Reason: {reason}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx: commands.Context, member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(
                    mutedRole,
                    speak=False,
                    send_messages=False,
                    read_message_history=True,
                    read_messages=True,
                )
        embed = discord.Embed(
            title="muted",
            description=f"{member.mention} was muted...",
            colour=discord.Colour.light_gray(),
        )
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f"You have been muted from: {guild.name}. Reason: {reason}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx: commands.Context, member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await member.send(f"You have unmutedd from: {ctx.guild.name}.")
        embed = discord.Embed(
            title="Unmute",
            description=f"{member.mention} was unmuted...",
            colour=discord.Colour.light_gray(),
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["purge", "delete"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = None):
        if amount == None:
            await ctx.channel.purge(limit=20)
        else:
            await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {amount} messages...")


def setup(bot):
    bot.add_cog(Moderation(bot))
