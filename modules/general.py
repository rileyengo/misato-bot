import discord
from discord.ext import commands

from utils import permissions
from random import choice

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        """about me"""
        embed=discord.Embed(title="misato", description="misato from evangelion \n discord.py ⋅ created 2018 ⋅ [repo](https://github.com/rileyengo/misato-bot)", color=0x4c4e9e)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/524084799586041867/898739625600884836/image0.jpg")
        await ctx.send(embed=embed)


    @commands.command()
    async def ping(self, ctx):
	    """ping!"""
	    await ctx.send('🏓 pong!')

    @commands.command() # possible @mention abuse :///
    async def mock(self, ctx, *, arg):
        """ rEpeAtS wHaT yOu sAy """
        await ctx.send(''.join(choice((str.upper, str.lower))(c) for c in arg)) 

    @commands.command()
    async def mocku(self, ctx, user: discord.User):
        """ mock someone else """
        channel = discord.utils.get(discord.Client().get_all_channels(), guild__name=discord.Guild.name, name=discord.TextChannel.name)
        msg = await channel.history().get(author__name=user)
        await ctx.send(''.join(choice((str.upper, str.lower))(c) for c in msg)) 

    @commands.command()
    async def avatar(self, ctx, user: discord.User or discord.Message.author):
	    """get a user's avatar (doesn't work rn)"""
	    await ctx.send(user.avatar_url)

def setup(bot):
    bot.add_cog(General(bot))