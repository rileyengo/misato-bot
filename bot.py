import discord
import os
# import datetime
from discord.ext import commands
from os import environ

bot = commands.Bot(command_prefix='?')
TOKEN = os.environ['TOKEN']
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='Evangelion 3.0+1.0'))

############################
### ?greet - hello there ###
############################ 

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

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

###################################
### ?katsuragi - goddamn embeds ###
###################################

@bot.command()
async def katsuragi(ctx):
	embed=discord.Embed(title='Misato Katsuragi', description='"Sometimes you need a little wishful thinking just to keep on living."', color=0x400080)
	embed.set_author(name='Misato Katsuragi',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp-bIMBDrqyGVeaIVK2zDlY9Vjvc8GxXml56C7ASiOeIVTEqqubw')
	embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp-bIMBDrqyGVeaIVK2zDlY9Vjvc8GxXml56C7ASiOeIVTEqqubw')
	embed.add_field(name='Gender', value='Female', inline=True)
	embed.add_field(name='Age', value=29, inline=True)
	embed.add_field(name='Affiliation', value='NERV', inline=True)
	embed.add_field(name='Position', value='Lieutenant Colonel', inline=True)
	embed.set_footer(text=discord.Message.author)
	await self.bot.say(embed=embed)

bot.run(TOKEN)
