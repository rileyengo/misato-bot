import discord
from discord.ext import commands

class GeneralCog:
	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def load(extension_name : str):
		"""Loads an extension."""
		try:
			bot.load_extension(extension_name)
		except (AttributeError, ImportError) as e:
			await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
			return
		await bot.say("{} loaded.".format(extension_name))

	@commands.command()
	async def unload(extension_name : str):
		"""Unloads an extension."""
		bot.unload_extension(extension_name)
		await bot.say("{} unloaded.".format(extension_name))

	###########################
	### ?dice - Roll a dice ###
	###########################

	@commands.command()
	async def roll(self, ctx, dice : str):
		"""Rolls a dice in NdN format."""
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await ctx.say('Format has to be in NdN!')
			return

		result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		await ctx.say(result)
		
	############################
	### ?greet - testing 123 ###
	############################
	@commands.command()
	async def greet(self, ctx):
		await ctx.say('you win yay')

def setup(bot):
    bot.add_cog(GeneralCog(bot))
