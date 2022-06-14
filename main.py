import discord
import aiohttp
from discord.ext import commands
from keepalive import keep_alive
import os
import random
import listas

############### Geral ###############

TOKEN = os.environ.get("secret")

client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
   print("Bot is currently online!")

############### Comandos ###############

@client.command (brief = "-> La Famila")
async def vin(ctx):
   await ctx.reply("La Familia")
  
@client.command (brief = "-> Dumb wisdom")
async def quote(ctx):
   await ctx.reply(random.choice(listas.quotes))

@client.command (brief = "-> Russian Roulette")
async def roulette(ctx):
   await ctx.reply(ctx.author.mention + random.choice(listas.roleta))

@client.command (brief = "-> Mega funny image")
async def pic(ctx):
   await ctx.reply(file=discord.File(random.choice(listas.imagens)))

@client.command(pass_context=True, brief = "-> meme from r/dankmemes")
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

############### Eventos ###############

@client.event
async def on_message(message):
  if message.author == client.user: 
    return
  
  msg = message.content

  sendM = message.channel.send

  if any(word in msg for word in listas.atts):
    await sendM("Diz bro <3")

  if any(word in msg for word in listas.bitch_words):
    await sendM("Smells like bitch in here")

  if any(word in msg for word in listas.bando_words):
    await sendM(random.choice(listas.bando_quote))

  await client.process_commands(message)

############### Keep_alive ###############

keep_alive()
client.run(TOKEN)