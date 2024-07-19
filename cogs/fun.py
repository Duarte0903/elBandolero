import listas
import discord
from discord.ext import commands
import random
import json
from PIL import Image
from io import BytesIO

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command (brief = "-> La Famila")
    async def vin(self, ctx):
      await ctx.reply("La Familia")

  
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


    @commands.command(brief="-> Dumb Wisdom")
    async def quote(self, ctx):
        try:
            with open("quotes.json", "r") as r:
                j = json.load(r)
                all_quotes = j["quotes"]
        except FileNotFoundError:
            await ctx.send("No quotes stored! Add them using the addQuote command.")
            return
    
        random_quote = random.choice(all_quotes)
        quote_text = random_quote["quote"]
    
        quote_message = f"**{quote_text}**"
        await ctx.send(quote_message)

  
    @commands.command(brief='-> command + "quote" to add a quote to the list')
    async def addQuote(self, ctx, quote_):
        def add_quote(quote, file="quotes.json"):
            with open(file, "r+") as fw:
                j = json.load(fw)
                j["quotes"].append({"quote": quote})
                with open(file, "w+") as wp:
                    wp.write(json.dumps(j))
        try:
            with open("quotes.json", "r"):
                pass
        except:
            with open("quotes.json", "w+") as wp:
                wp.write('{"quotes" : []}')
        finally:
            add_quote(quote_)
            await ctx.send("Done!")

  
    @commands.command(brief='-> command + "name" to add a new name to the list')
    async def addName(self, ctx, name_):
        def add_name(name, file="lopes.json"):
            with open(file, "r+") as fw:
                j = json.load(fw)
                j["names"].append(name)
                with open(file, "w+") as wp:
                    wp.write(json.dumps(j))
        try:
            with open("lopes.json", "r"):
                pass
        except:
            with open("lopes.json", "w+") as wp:
                wp.write('{"names" : []}')
        finally:
            add_name(name_)
            await ctx.send("Done!")

  
    @commands.command(brief="-> Keep track of the longest nickname in history")
    async def lopes(self, ctx):
      try:
        with open("lopes.json", "r") as r:
            j = json.load(r)
            all_names = j["names"]
            full_name = ""
            for name in all_names:
              full_name += str(name) + " "
      except:
        await ctx.send("Empty name")
        return
      await ctx.send(full_name)


    @commands.command(brief='-> command + @member to make them gay')
    async def lgbt(self, ctx, member: discord.Member):
        avatar_url = member.avatar_url_as(format='png')
        response = await avatar_url.read()
        profile_picture = Image.open(BytesIO(response)).convert('RGBA')
    
        overlay_image = Image.open('assets/lgbt.png').convert('RGBA')
    
        overlay_image = overlay_image.resize(profile_picture.size)
    
        if profile_picture.mode != 'RGBA':
            profile_picture = profile_picture.convert('RGBA')
    
        opacity = 0.5 
        overlay_image = overlay_image.copy()
        overlay_image.putalpha(int(255 * opacity))  
    
        merged_image = Image.alpha_composite(profile_picture, overlay_image)
    
        result_buffer = BytesIO()
        merged_image.save(result_buffer, format='PNG')
        result_buffer.seek(0)
    
        await ctx.send(file=discord.File(result_buffer, filename='overlay.png'))

    @commands.command(brief='-> Racist score')
    async def racistScore(self, ctx): 
      embed = discord.Embed(
        title="Racist Score", 
        color=0xff7b00
      )

      try:
        with open('racist_score.json', 'r') as file:
          racist_scores = json.load(file)

        for member_id, score in racist_scores.items(): 
          member = ctx.guild.get_member(int(member_id))
          if member:
              nickname = member.nick if member.nick else member.display_name
              embed.add_field(name=f"{nickname}", value=f"N word counter: {score}", inline=False)
          else:
              print(f"Member not found for user ID: {member_id}")

        await ctx.send(embed=embed)

      except FileNotFoundError:
        await ctx.send("Racist score data not found.")
      except Exception as e:
        print(f"An error occurred: {str(e)}")
      

def setup(bot):
    bot.add_cog(Fun(bot))