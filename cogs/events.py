from discord.ext import commands
from discord.utils import get
import listas
import random
import json


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
      role = get(member.guild.roles, id=811682375456784404)
      await member.add_roles(role)
      welcome_message = f"oh crikey it's the albanian rozzers !!!"
      await member.send(welcome_message)

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.author == self.bot.user: 
        return
  
      msg = message.content

      sendM = message.channel.send

      if msg == "@everyone":
        await sendM("What's up bro <3")

      if any(word in msg for word in listas.bando_words):
        await sendM(random.choice(listas.bando_quote))

      if any(word in msg for word in listas.racist_words):
        author = str(message.author.id)

        try:
          with open('racist_score.json', 'r') as file:
            racist_scores = json.load(file)

            if author in racist_scores:
              racist_scores[author] += 1
              
            else:
              racist_scores[author] = 1

            sorted_racist_scores = dict(sorted(racist_scores.items(), key=lambda item: item[1], reverse=True))

            with open('racist_score.json', 'w') as file:
              json.dump(sorted_racist_scores, file, indent=4)
              await sendM("Racist score updated")

        except FileNotFoundError:
          pass
          

def setup(bot):
    bot.add_cog(Events(bot))