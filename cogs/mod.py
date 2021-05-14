import discord
import asyncio
import json
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands

extension = ".py"
bot = commands.Bot(command_prefix='::')

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clearchannel(self, ctx, amount=10000):
        await ctx.channel.purge(limit=amount)
        embed=discord.Embed(title="", description="**Clear**", color=0xff5917)
        embed.set_author(name="Doggo Commands",   icon_url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
        embed.add_field(name="`❌Clear❌`", value="I have cleared the channel.",   inline=True)
        embed.set_footer(text="Created by Farm Merchant#9926",icon_url="https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/cd/Wooden_Hoe_JE3_BE3.png/revision/latest/scale-to-width-down/150?cb=20200226194121")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount :int = -1):
          await ctx.channel.purge(limit=amount)
          embed=discord.Embed(title="", description="**Clear**", color=0xff5917)
          embed.set_author(name="Doggo Clear",icon_url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
          embed.set_thumbnail(url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
          embed.add_field(name="`❌Clear❌`", value="You have cleared messages.", inline=True)   
          embed.set_footer(text="Created by Farm Merchant#9926", icon_url="https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/cd/Wooden_Hoe_JE3_BE3.png/revision/latest/scale-to-width-down/150?cb=20200226194121")
          await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
      await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
      await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx,* , member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
        user =  ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
          await ctx.guild.unban(user)
          await ctx.send(f'Unbanned {user.mention}')
          return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, user : discord.Member, *, reason=None):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role in ctx.guild.roles:
            await user.add_roles(muted_role)
            await ctx.send(f'{user.mention} was muted for: ' '{}.'.format(reason))
        else:
            perms = discord.Permissions()
            perms.send_messages = False
            muted_role = await ctx.guild.create_role(name="Muted", permissions = perms)
            await user.add_roles(muted_role)
            await ctx.send(f'{user.mention} was muted for: ' '{}.'.format(reason))

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def tempmute(self, ctx, member: discord.Member,time):
        muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
        time_convert = {"s":1, "m":60, "h":3600,"d":86400}
        tempmute= int(time[0]) * time_convert[time[ -1]]
        await ctx.message.delete()
        await member.add_roles(muted_role)
        embed = discord.Embed(description= f"✅ **{member.display_name}#{member.discriminator} muted successfuly**", color=discord.Color.green())
        await ctx.send(embed=embed, delete_after=5)
        await asyncio.sleep(tempmute)
        await member.remove_roles(muted_role)
 
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, user : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role in user.roles:
            await user.remove_roles(role)
            ctx.send(f"{user.mention} has been unmuted.")
        else:
            ctx.send(f"{user.mention} is not muted.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx):
        guild = ctx.guild
        await ctx.message.channel.set_permissions(guild.default_role,send_messages = False)
        await ctx.send("🔒 Channel locked.")
 
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx):
        guild = ctx.guild
        await ctx.message.channel.set_permissions(guild.default_role,send_messages = True)
        await ctx.send("🔒 Channel unlocked.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def warn(self, ctx, user:discord.User, *reason:str):
      if not reason:
        await ctx.send("Please provide a reason")
        return
      reason = ' '.join(reason)
      for current_user in report['users']:
        if current_user['name'] == user.name:
          current_user['reasons'].append(reason)
          break
      else:
        report['users'].append({
          'name':user.name,
          'reasons': [reason,]
        })
      with open('reports.json','w+') as f:
        json.dump(report,f)

    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def warnings(self, ctx ,user:discord.User):
      for current_user in report['users']:
        if user.name == current_user['name']:
          await ctx.send(f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
          break
      else:
        await ctx.send(f"{user.name} has never been reported")  

    @warn.error
    async def kick_error(error, ctx):
      if isinstance(error, MissingPermissions):
          text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
          await ctx.send(ctx.message.channel, text) 

def setup(bot):
    bot.add_cog(Mod(bot))
