import discord
import os
import datetime
import sys, traceback
from discord.ext import commands
from os import environ

bot = commands.Bot(command_prefix='?')
TOKEN = os.environ['TOKEN']
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
    await bot.change_presence(activity=discord.Game(name='𝙛𝙡𝙮 𝙢𝙚 𝙩𝙤 𝙩𝙝𝙚 𝙢𝙤𝙤𝙣'))

##################################
### LOAD AND UNLOAD EXTENSIONS ###
##################################
if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()
bot.run(TOKEN, bot=True, reconnect=True)
