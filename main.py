import discord
import os
import aiohttp
import nacl
from discord import FFmpegPCMAudio
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from discord.utils import get
from keepalive import keep_alive
import random
import listas

############### Geral ###############

TOKEN = os.environ.get("secret")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "$", intents=intents)

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

@bot.command(brief="-> command + @user + <role> to give a specific role")
@commands.has_permissions(manage_roles = True)
async def addRole(ctx, user : discord.Member, role:discord.Role):
    await user.add_roles(role)
    await ctx.send(f" Added {role} role to {user.mention}")

@addRole.error
async def role_error(self,ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are not authorized for this action")

@bot.command(pass_context=True, brief="-> commnad + @member + role to remove role")
@commands.has_permissions(manage_roles = True)
async def deleteRole(ctx, user : discord.Member, role_name):
    role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
    await role_object.delete()
    await ctx.send(f"{user.mention} is no longer {role_object}")

@deleteRole.error
async def delete_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are not authorized for this action")
      
@bot.command(brief="-> command + @member to kick a member")
@has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member,*,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'The User {member.mention} has been kicked from the server')

@kick.error
async def kick_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You do not have required permission for the action performed")

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

@bot.event 
async def on_member_join(member):
  role = get(member.guild.roles, id=811682375456784404)
  await member.add_roles(role)

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