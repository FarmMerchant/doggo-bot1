import discord
import datetime
from discord.ext import commands

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def botinfo(self, ctx):
      embed=discord.Embed(title="Doggo", description="Doggo is currently being worked on.", color=0xff5917)
      embed.add_field(name="**Creation Date**", value="`Doggo was made on April 3, 2021`", inline=False)
      embed.add_field(name="Command Prefix", value="`::`", inline=False)
      embed.set_footer(text="Created by Farm Merchant#9926")
      await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
