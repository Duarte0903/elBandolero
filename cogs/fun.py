import listas
import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command (brief = "-> La Famila")
    async def vin(self, ctx):
      await ctx.reply("La Familia")

    @commands.command (brief = "-> Dumb wisdom")
    async def quote(self, ctx):
      await ctx.reply(random.choice(listas.quotes))

    @commands.command (brief = "-> Russian Roulette")
    async def roulette(self, ctx):
       await ctx.reply(ctx.author.mention + random.choice(listas.roleta))

    @commands.command (brief = "-> Mega funny image")
    async def pic(self, ctx):
       await ctx.reply(file=discord.File(random.choice(listas.imagens)))

    @commands.command(brief = "-> Get pp size")
    async def size(self, ctx):
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

    @commands.command(brief = "-> Casually nuke your mate")
    async def nuke(self, ctx, member:discord.Member):
      await ctx.send (f"{ctx.author.mention} just nuked {member.mention}")
      await ctx.send ("Here comes the sun 🌞")

def setup(bot):
    bot.add_cog(Fun(bot))