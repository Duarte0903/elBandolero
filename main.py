import discord
import os
from discord.ext import commands
from keepalive import keep_alive

TOKEN = os.environ.get("secret")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "$", intents=intents)

@bot.event
async def on_ready():
  print("Bot is currently online!")
  await bot.change_presence(activity = discord.Game(name = '$help'))

def loadCogs():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            bot.load_extension(f"cogs.{name}")
            print(f"Loaded cogs.{name}")

loadCogs()

keep_alive()
bot.run(TOKEN)