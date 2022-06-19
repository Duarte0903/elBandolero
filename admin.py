import discord
import os
from discord.ext import commands
from discord.utils import get

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    