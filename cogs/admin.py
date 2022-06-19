import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="-> command + @user + <role> to give a specific role")
    @commands.has_permissions(manage_roles = True)
    async def addRole(self, ctx, user : discord.Member, role:discord.Role):
        await user.add_roles(role)
        await ctx.send(f" Added {role} role to {user.mention}")

    @addRole.error
    async def role_error(self,ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are not authorized for this action")

    @commands.command(pass_context=True, brief="-> commnad + <role> to delete a role")
    @commands.has_permissions(manage_roles = True)
    async def deleteRole(self, ctx, role_name):
        role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
        await role_object.delete()
        await ctx.send("Role deleted")

    @deleteRole.error
    async def delete_error(self, ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are not authorized for this action")
      
    @commands.command(brief="-> command + @member to kick a member")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member,*,reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'The User {member.mention} has been kicked from the server')

    @kick.error
    async def kick_error(self, ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You do not have required permission for the action performed")

def setup(bot):
    bot.add_cog(Admin(bot))