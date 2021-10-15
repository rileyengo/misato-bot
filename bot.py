import discord
import os
import datetime
import sys, traceback
from discord.ext import commands

bot = commands.Bot(command_prefix="?")
TOKEN = os.getenv("TOKEN")
startup_extensions = ['cogs.general']
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='if you\'re reading this then i am merely a shell of my former existence with no cogs 🤩'))

##################################
### LOAD AND UNLOAD EXTENSIONS ###
##################################
# if __name__ == '__main__':
#    for extension in startup_extensions:
#        bot.load_extension(extension)

bot.run(TOKEN, bot=True, reconnect=True)
