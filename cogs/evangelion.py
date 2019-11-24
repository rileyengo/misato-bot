import discord
from discord.ext import commands
import datetime

class Evangelion:
	def __init__(self, bot):
		self.bot = bot
	
	#######################
	###### CHARACTERS #####
	#######################

	@commands.group(name='character', pass_context=True, aliases=['char', 'c', 'cinfo'])
	async def character(self, ctx):
		"""Stats on Evangelion characters."""
		if ctx.invoked_subcommand is None:
			await ctx.send(':x: Please specify a character!')

	@character.command(name='misato', aliases=['katsuragi', 'Misato'])
	async def misato(self, ctx):
		embed=discord.Embed(title='Misato Katsuragi', description='"Sometimes you need a little wishful thinking just to keep on living."', color=0x400080)
		embed.set_author(name='Misato Katsuragi',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp-bIMBDrqyGVeaIVK2zDlY9Vjvc8GxXml56C7ASiOeIVTEqqubw')
		embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp-bIMBDrqyGVeaIVK2zDlY9Vjvc8GxXml56C7ASiOeIVTEqqubw')
		embed.add_field(name='Gender', value='Female', inline=True)
		embed.add_field(name='Age', value=29, inline=True)
		embed.add_field(name='Affiliation', value='NERV', inline=True)
		embed.add_field(name='Title', value='Lieutenant Colonel', inline=True)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@character.command(name='shinji', aliases=['ikari', 'Shinji', 'Ikari'])
	async def shinji(self, ctx):
		embed=discord.Embed(title='Shinji Ikari', description='"I thought this was supposed to be a world without pain."', color=1655179)
		embed.set_author(name='Shinji Ikari',icon_url='https://pbs.twimg.com/media/CqOGa3PWIAAc6LZ.jpg')
		embed.set_thumbnail(url='http://images6.fanpop.com/image/quiz/1036000/1036067_1377237548381_500_375.jpg')
		embed.add_field(name='Gender', value='Male', inline=True)
		embed.add_field(name='Age', value=14, inline=True)
		embed.add_field(name='Affiliation', value='NERV', inline=True)
		embed.add_field(name='Title', value='Third Child', inline=True)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@character.command(name='asuka', aliases=['Asuka', 'Langley'])
	async def asuka(self, ctx):
		if ctx.invoked_subcommand is 'rebuild' or 'shikinami' or 'langley shikinami' or 'shikinami langley':
			asukaname = 'Asuka Shikinami Langley'
			picture = 'http://s1.narvii.com/image/5fm7u2qd7j3jovegts53xidwfuxjgrwt_00.jpg'
			quote = '"Pretending to have fun with others will only wear me out."'
		else:
			asukaname = 'Asuka Langley Soryu'
			picture = 'https://vignette.wikia.nocookie.net/evangelion/images/a/a7/Asuka_smiling.png/'
			quote = '"It is simply the duty of the elite to protect the ignorant masses."'
		embed=discord.Embed(title=asukaname, description=quote, color=13632027)
		embed.set_author(name=asukaname,icon_url='https://pbs.twimg.com/profile_images/801087906/Asuka_Twitterpic_400x400.jpg')
		embed.set_thumbnail(url=picture)
		embed.add_field(name='Gender', value='Female', inline=True)
		embed.add_field(name='Age', value=14, inline=True)
		embed.add_field(name='Affiliation', value='NERV', inline=True)
		embed.add_field(name='Position', value='Second Child', inline=True)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@character.command(name='rei', aliases=['ayanami', 'Rei', 'Ayanami'])
	async def rei(self, ctx):
		embed=discord.Embed(title='Rei Ayanami', description='"Those who hate themselves, cannot love or trust others."', color=7250141)
		embed.set_author(name='Rei Ayanami',icon_url='https://66.media.tumblr.com/00c2934a0314d1b7a84596e2fa556bed/tumblr_oju52h8S441vy2tgqo4_400.png')
		embed.set_thumbnail(url='https://66.media.tumblr.com/00c2934a0314d1b7a84596e2fa556bed/tumblr_oju52h8S441vy2tgqo4_400.png')
		embed.add_field(name='Gender', value='Female', inline=True)
		embed.add_field(name='Age', value=14, inline=True)
		embed.add_field(name='Affiliation', value='NERV', inline=True)
		embed.add_field(name='Title', value='First Child', inline=True)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@character.command(name='kaworu', aliases=['nagisa', 'Kaworu', 'Nagisa'])
	async def kaworu(self, ctx):
		embed=discord.Embed(title='Kaworu Nagisa', description='"Maybe I was born to meet you."', color=75600)
		embed.set_author(name='Kaworu Nagisa',icon_url='https://66.media.tumblr.com/a6dbc3ec67b3664f6fbc001a37f096c5/tumblr_inline_p7ief68sXM1skorrd_540.png')
		embed.set_thumbnail(url='https://66.media.tumblr.com/a6dbc3ec67b3664f6fbc001a37f096c5/tumblr_inline_p7ief68sXM1skorrd_540.png')
		embed.add_field(name='Gender', value='Male', inline=True)
		embed.add_field(name='Age', value=15, inline=True)
		embed.add_field(name='Affiliation', value='SEELE', inline=True)
		embed.add_field(name='Title', value='Fifth Child, Seventeenth Angel', inline=True)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@character.command(name='gendo', aliases=['Gendo', 'gendo ikari', 'Gendo Ikari'])
	async def gendo(self, ctx):
		embed=discord.Embed(title='Gendo Ikari', description='"Mankind\'s greatest fear is Mankind itself."', color=75600)
		embed.set_author(name='Gendo Ikari',icon_url='https://pbs.twimg.com/profile_images/779243168130736128/_Q24gTBh_400x400.jpg')
		embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/evangelion/images/8/8c/Weaving_a_Story.png')
		embed.add_field(name='Gender', value='Male', inline=True)
		embed.add_field(name='Age', value=48, inline=True)
		embed.add_field(name='Affiliation', value='NERV', inline=True)
		embed.add_field(name='Title', value='Commander', inline=True)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)
	
	########################
	###### EVANGELIONS #####
	########################
	
	@commands.group(name='evangelion', pass_context=True, aliases=['mech', 'mecha', 'eva', 'robot', 'unit'])
	async def evangelion(self, ctx):
		"""Stats on Evangelion mechas."""
		if ctx.invoked_subcommand is None:
			await ctx.send(':x: Please specify a unit!')
			
	@evangelion.command(name='01', aliases=['unit 01', 'unit-01', 'shinji']) # Not quite finished yet lol
	async def unit1(self, ctx):
		embed=discord.Embed(title='Unit-01', description='', color=75600)
		embed.set_author(name='Evangelion Unit-01',icon_url='https://pbs.twimg.com/profile_images/779243168130736128/_Q24gTBh_400x400.jpg')
		embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/evangelion/images/2/2c/Evangelion_Unit-01_front1.png/revision/latest?cb=20190520193846')
		embed.add_field(name='Color', value='Purple', inline=True)
		embed.add_field(name='Pilot', value='Shinji Ikari', inline=True)
		embed.add_field(name='Location', value='Tokyo', inline=True)
		embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	#@evangelion.command(name='02', aliases=['unit 02', 'unit-02', 'asuka']) # Not quite finished yet lol
	#async def unit1(self, ctx):
		#embed=discord.Embed(title='Unit-02', description='', color=75600)
		#embed.set_author(name='Evangelion Unit-02',icon_url='https://pbs.twimg.com/profile_images/779243168130736128/_Q24gTBh_400x400.jpg')
		#embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/evangelion/images/8/8c/Weaving_a_Story.png')
		#embed.add_field(name='Color', value='Red', inline=True)
		#embed.add_field(name='Pilot', value='Asuka Soryu Langley\u200BAsuka Shikinami Langley', inline=True)
		#embed.add_field(name='Location', value='Tokyo', inline=True)
		#embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
		#await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Evangelion(bot)) # find some way to hide this from ?help
