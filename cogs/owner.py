import discord
from discord.ext import commands

class Owner:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='owner')
	@commands.is_owner()
		async def owner(self, ctx):
		"""Only the owner can use this. Shh."""
			await ctx.send('You are an official affiliated with SEELE.')

def setup(bot):
    bot.add_cog(Owner(bot))
