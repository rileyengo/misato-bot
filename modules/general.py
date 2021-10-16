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

    @commands.command()
    async def avatar(self, user: discord.User, ctx):
	    """get a user's avatar"""
	    await ctx.send(user.avatar_url)

def setup(bot):
    bot.add_cog(General(bot))