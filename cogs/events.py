from discord.ext import commands
from discord.utils import get


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
      role = get(member.guild.roles, id=811682375456784404)
      await member.add_roles(role)


def setup(bot):
    bot.add_cog(Events(bot))