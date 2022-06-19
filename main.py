import discord
import os
import aiohttp
import nacl
from discord import FFmpegPCMAudio
from discord.ext import commands
from keepalive import keep_alive
import random
import listas

############### Geral ###############

TOKEN = os.environ.get("secret")

bot = commands.Bot(command_prefix = "$")

@bot.event
async def on_ready():
  print("Bot is currently online!")
  
############### Comandos ###############
      
@bot.command (brief = "-> La Famila")
async def vin(ctx):
  await ctx.reply("La Familia")

@bot.command (brief = "-> Dumb wisdom")
async def quote(ctx):
  await ctx.reply(random.choice(listas.quotes))

@bot.command (brief = "-> Russian Roulette")
async def roulette(ctx):
   await ctx.reply(ctx.author.mention + random.choice(listas.roleta))

@bot.command (brief = "-> Mega funny image")
async def pic(ctx):
   await ctx.reply(file=discord.File(random.choice(listas.imagens)))

@bot.command(pass_context=True, brief = "-> meme from r/dankmemes")
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(brief = "-> Get pp size")
async def size(ctx):
  str = "8"
  num = random.randint(5, 100)
  res = str.ljust(num + len(str), "-")
  await ctx.reply(res+"D")
  if num <= 25:
   await ctx.reply(ctx.author.mention + "  Damn bro, that's small 😬")
  elif num >= 60:
    await ctx.reply(ctx.author.mention + "  Walking must be a problem uh 🍖")
  else:
    await ctx.reply(ctx.author.mention + "  Avarage is just fine ❤️")

@bot.command(brief = "-> Casually nuke your mate")
async def nuke(ctx, member:discord.Member):
  await ctx.send (f"{ctx.author.mention} just nuked {member.mention}")
  await ctx.send ("Here comes the sun 🌞")

############### Eventos ###############

@bot.event
async def on_message(message):
  if message.author == bot.user: 
    return
  
  msg = message.content

  sendM = message.channel.send

  if any(word in msg for word in listas.atts):
    await sendM("Diz bro <3")

  if any(word in msg for word in listas.bitch_words):
    await sendM("Smells like bitch in here")

  if any(word in msg for word in listas.bando_words):
    await sendM(random.choice(listas.bando_quote))

  await bot.process_commands(message)

############### Audio ####################

@bot.command(pass_context=True, brief="-> Bot joins voice channel")
async def join(ctx):

    if(ctx.author.voice):

        channel = ctx.message.author.voice.channel

        voice=await channel.connect() 

    else:

        await ctx.send("please join voice channel")


@bot.command(brief="-> Bot leaves voice channel")
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

############### Keep_alive ###############

keep_alive()
bot.run(TOKEN)