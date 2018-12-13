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
    client.change_presence(*, game=discord.Game(name='NERV HQ'))

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
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(':dice:' + result)

###################################
### ?katsuragi - goddamn embeds ###
###################################

@bot.command()
async def katsuragi(ctx):
	embed = discord.Embed(colour=discord.Colour(0x45168b), url="https://discordapp.com", description="**Misato** is the operations director at NERV, initially with the rank of captain; she is later promoted to major.", timestamp=datetime.datetime.now())
	embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp-bIMBDrqyGVeaIVK2zDlY9Vjvc8GxXml56C7ASiOeIVTEqqubw")
	embed.set_author(name="Misato Katsuragi", icon_url="https://pbs.twimg.com/profile_images/729166941/Misato_Katsuragi_400x400.jpg")
	embed.set_footer(text=message.author, icon_url=discord.message.author.avatar_url)
	embed.add_field(name="Position", value="Lieutenant Colonel", inline=True)
	embed.add_field(name="Affiliation", value="NERV", inline=True)
	embed.add_field(name="Popularity", value="#1", inline=True)
	embed.add_field(name="Beers drunk today", value="69", inline=True)
	await bot.say(embed=embed)

bot.run(TOKEN)
