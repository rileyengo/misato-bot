import discord
from discord.ext import commands

from utils import permissions
from random import choice

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
	    """ping!"""
	    await ctx.send('🏓 pong!')

    @commands.command()
    async def mock(self, ctx, *, arg):
        """ rEpeAtS wHaT yOu sAy """
        await ctx.send(''.join(choice((str.upper, str.lower))(c) for c in arg)) 

def setup(bot):
    bot.add_cog(General(bot))