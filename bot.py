import discord
import os
import datetime
import sys, traceback
from discord.ext import commands

bot = commands.Bot(command_prefix="?")
TOKEN = os.getenv("TOKEN")
startup_extensions = ['cogs.evangelion', 
                      'cogs.general', 
                      'cogs.members', 
                      'cogs.rng'
                     ]
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='get in we\'re going to therapy'))

##################################
### LOAD AND UNLOAD EXTENSIONS ###
##################################
if __name__ == '__main__':
    for extension in startup_extensions:
        bot.load_extension(extension)

bot.run(TOKEN, bot=True, reconnect=True)
