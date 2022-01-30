import discord
from discord.ext import commands
import json


class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def update_data(self, users, user):
        if not f'{user.id}' in users:
            users[f'{user.id}'] = {}
            users[f'{user.id}']['experience'] = 0
            users[f'{user.id}']['level'] = 1

    async def add_experience(self, users, user, exp):
        users[f'{user.id}']['experience'] += exp

    async def level_up(self, users, user, message):
        experience = users[f'{user.id}']['experience']
        lvl_start = users[f'{user.id}']['level']
        lvl_end = int(experience ** (1 / 4))
        if lvl_start < lvl_end:
            await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
            users[f'{user.id}']['level'] = lvl_end

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == False:
            with open('cogs/levels.json', 'r') as f:
                users = json.load(f)

            await self.update_data(users, message.author)
            await self.add_experience(users, message.author, 5)
            await self.level_up(users, message.author, message)

            with open('cogs/levels.json', 'w') as f:
                json.dump(users, f)

    @commands.command(aliases=["rank", "lvl"])
    async def level(self, ctx, member: discord.Member = None):
        if not member:
            id = ctx.message.author.id
            with open('cogs/levels.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            await ctx.send(f'You are at level {lvl} now!')
        else:
            id = member.id
            with open('cogs/levels.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            await ctx.send(f'{member.mention} is at level {lvl} now!')


def setup(bot):
    bot.add_cog(Level(bot))
