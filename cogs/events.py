from discord.ext import commands
from discord.utils import get
import listas
import random


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
      role = get(member.guild.roles, id=811682375456784404)
      await member.add_roles(role)

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


def setup(bot):
    bot.add_cog(Events(bot))