import discord
from discord.ext import commands

class General:
	def __init__(self, bot):
		self.bot = bot
	@commands.command(name='load')
	@commands.is_owner()
	async def load(ctx, extension_name : str):
		"""Loads an extension."""
		try:
			bot.load_extension(extension_name)
		except (AttributeError, ImportError) as e:
			await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
			return
		await bot.say("{} loaded.".format(extension_name))

	@commands.command(name='unload')
	@commands.is_owner()
	async def unload(ctx, extension_name : str):
		"""Unloads an extension."""
		bot.unload_extension(extension_name)
		await ctx.send("{} unloaded.".format(extension_name))

	@commands.command(name='ping')
	async def ping(self, ctx):
		"""Ping!"""
		await ctx.send('Pong!')
		
	@commands.command(name='repeat')
	async def repeat(ctx, *, arg):
		"""Repeats what you say."""
		await ctx.send(arg)

def setup(bot):
    bot.add_cog(General(bot))
