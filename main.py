import discord
import os
from discord.ext import commands
from keepalive import keep_alive
from discord.ext import tasks
from itertools import cycle

TOKEN = os.environ.get("secret")

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)

status = cycle(['your mom','your mom'])

@bot.event
async def on_ready():
    change_status.start()
    print("Bot is currently online!")
    await bot.change_presence(activity=discord.Game(name='your mom'))

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

def loadCogs():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            bot.load_extension(f"cogs.{name}")
            print(f"Loaded cogs.{name}")


loadCogs()

keep_alive()
bot.run(TOKEN)
