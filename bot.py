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

@bot.group(pass_context=True)
async def character(ctx):
	if ctx.invoked_subcommand is None:
		await ctx.send(':x: Please specify a character!')

@character.command()
async def misato(ctx):
	embed=discord.Embed(title='Misato Katsuragi', description='"Sometimes you need a little wishful thinking just to keep on living."', color=0x400080)
	embed.set_author(name='Misato Katsuragi',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp-bIMBDrqyGVeaIVK2zDlY9Vjvc8GxXml56C7ASiOeIVTEqqubw')
	embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp-bIMBDrqyGVeaIVK2zDlY9Vjvc8GxXml56C7ASiOeIVTEqqubw')
	embed.add_field(name='Gender', value='Female', inline=True)
	embed.add_field(name='Age', value=29, inline=True)
	embed.add_field(name='Affiliation', value='NERV', inline=True)
	embed.add_field(name='Title', value='Lieutenant Colonel', inline=True)
	embed.set_footer(text=discord.Message.author)
	await ctx.send(embed=embed)

@character.command()
async def shinji(ctx):
	embed=discord.Embed(title='Shinji Ikari', description='"I thought this was supposed to be a world without pain."', color=1655179)
	embed.set_author(name='Shinji Ikari',icon_url='http://images6.fanpop.com/image/quiz/1036000/1036067_1377237548381_500_375.jpg')
	embed.set_thumbnail(url='http://images6.fanpop.com/image/quiz/1036000/1036067_1377237548381_500_375.jpg')
	embed.add_field(name='Gender', value='Male', inline=True)
	embed.add_field(name='Age', value=14, inline=True)
	embed.add_field(name='Affiliation', value='NERV', inline=True)
	embed.add_field(name='Title', value='Third Child', inline=True)
	embed.set_footer(text=discord.Message.author)
	await ctx.send(embed=embed)

@character.command()
async def asuka(ctx):
	if ctx.invoked_subcommand is 'rebuild' or 'shikinami' or 'langley shikinami' or 'shikinami langley':
		embed=discord.Embed(title='Asuka Shikinami Langley', description='"Pretending to have fun with others will only wear me out."', color=13632027)
		embed.set_author(name='Asuka Shikinami Langley',icon_url='http://s1.narvii.com/image/5fm7u2qd7j3jovegts53xidwfuxjgrwt_00.jpg')
		embed.set_thumbnail(url='http://s1.narvii.com/image/5fm7u2qd7j3jovegts53xidwfuxjgrwt_00.jpg')
		embed.add_field(name='Gender', value='Female', inline=True)
		embed.add_field(name='Age', value=14, inline=True)
		embed.add_field(name='Affiliation', value='NERV', inline=True)
		embed.add_field(name='Position', value='Second Child', inline=True)
		embed.set_footer(text=discord.Message.author)
		await ctx.send(embed=embed)
	else:
		embed=discord.Embed(title='Asuka Langley Soryu', description='"It is simply the duty of the elite to protect the ignorant masses."', color=13632027)
		embed.set_author(name='Asuka Langley Soryu',icon_url='https://vignette.wikia.nocookie.net/evangelion/images/a/a7/Asuka_smiling.png/')
		embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/evangelion/images/a/a7/Asuka_smiling.png/')
		embed.add_field(name='Gender', value='Female', inline=True)
		embed.add_field(name='Age', value=14, inline=True)
		embed.add_field(name='Affiliation', value='NERV', inline=True)
		embed.add_field(name='Position', value='Second Child', inline=True)
		embed.set_footer(text=discord.Message.author)
		await ctx.send(embed=embed)

bot.run(TOKEN)
