import discord
import datetime
from discord.ext import commands,tasks

bot = commands.Bot(command_prefix="us.")

@tasks.loop(seconds=1)
async def servers():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name=f"Among Us"))

@bot.event
async def on_ready():
  servers.start()

@bot.command()
async def help(message):
  embed = discord.Embed(title="Among Us Help",color=discord.Color.green())
  embed.add_field(name="us.setup",value="This command is used for setting up the bot when bot arrives into the server. The bot creates a channel named **among-us**.")
  embed.add_field(name="us.post", value="This command is used for posting your game code with other users. This only takes a 6 letter code and no other things.")
  embed.add_field(name="Additional feature",value="You can chat in the bot's DM it works as a mod mail.")
  embed.set_footer(text="Prefix: us.")
  await message.channel.send(embed=embed)
  
@bot.command()
async def setup(message):
  if discord.utils.get(message.guild.channels,name="among-us"):
    await message.channel.send("There is a pre-existing channel named **among-us** all the codes will be redirected to that channel!!")
  else:
    await message.guild.create_text_channel(name="among-us")
    channel = discord.utils.get(message.guild.channels,name="among-us")
    await channel.send("***Note: Do not change this channel's name***")   
  
@bot.command()
async def post(message,code):
  digits = '0123456789'
  if len(code) > 6:
    await message.channel.send(f"The code must be 6 letters!!")
  else:
    for i in code:
      if i in digits:
        await message.channel.send("The code must not contain any number.")
        break
      elif i in '/.,\'\"\\;:~`-_+=}{[]*^%$#@!&()':
        await message.channel.send("The code must be alphabetical")
        break
      else:
        await message.message.delete()
        for guild in bot.guilds:
            channel = discord.utils.get(guild.channels,name="among-us")
            embed = discord.Embed(description=f"**{code.upper()}**",color=discord.Color.red(),timestamp=message.created_at)
            embed.set_author(name=f"{message.author.name}#{message.author.discriminator}",icon_url=message.author.avatar_url)
            embed.set_footer(text=f"{message.guild.name",icon_url=message.guild.icon_url)
            channel.send(embed=embed)

@bot.event
async def on_message(message):
  if isinstance(message.channel,discord.DMChannel):
    embed = discord.Embed(description=message.content,color=discord.Color.green())
    embed.set_author(name="{message.author.name}#{message.author.discriminator}",icon_url=message.author.avatar_url)
    category = dicord.utils.get(bot.get_guild(752334684595290143).categories,name="Among Us Mod Mail")
            
bot.run("NzYyNTA2MjA4MjkxODQ4MjEy.X3qJPg.zoBQ9je5TJHtKAQtuCotXjOZsEU")
