import discord
import aiohttp
from discord.ext import commands
import random

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief = "-> meme from r/dankmemes")
    async def meme(self, ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(pass_context=True, brief = "-> F1 wallpaper from r/F1Porn")
    async def f1(self, ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/F1Porn/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Reddit(bot))