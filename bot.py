import discord
import os
import datetime
from discord.ext import commands
from os import environ

bot = commands.Bot(command_prefix='?')
TOKEN = os.environ['TOKEN']
startup_extensions = ["characters"]
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='Evangelion 3.0+1.0'))

###########################
### LOAD AND UNLOAD EXTENSIONS ###
###########################
@bot.command()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        ctx.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    ctx.unload_extension(extension_name)
    await ctx.say("{} unloaded.".format(extension_name))

###########################
### ?dice - Roll a dice ###
###########################

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.send(':dice: ' + result)
# extensions
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(TOKEN)
