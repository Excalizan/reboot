import discord
from discord.ext import commands


class Error_Handler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener() 
    async def on_command_error(self, ctx, error): 
        if isinstance(error, commands.CommandNotFound): 
            em = discord.Embed(title=f"Error!", description=f"Command not found with that name!", color=discord.Colour.red()) 
            await ctx.send(embed=em)

        if isinstance(error, commands.CommandOnCooldown):
            day = round(error.retry_after/86400)
            hour = round(error.retry_after/3600)
            minute = round(error.retry_after/60)
            if day > 0:
                await ctx.send('This command has a cooldown, for '+str(day)+ "day(s)")
            elif hour > 0:
                await ctx.send('This command has a cooldown, for '+str(hour)+ " hour(s)")
            elif minute > 0:
                await ctx.send('This command has a cooldown, for '+ str(minute)+" minute(s)")
            else:
                await ctx.send(f'This command has a cooldown, for {error.retry_after:.2f} second(s)')
        
        if isinstance(error, commands.UserNotFound):
            em = discord.Embed(title=f"Error!", description=f"The provided user was not found!", color=discord.Colour.red())
            await ctx.send(embed=em)



def setup(bot):
    bot.add_cog(Error_Handler(bot))
