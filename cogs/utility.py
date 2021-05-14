import discord
import random
import os
import asyncio
import datetime
import aiohttp
import re
import json
import utils
import sys
import youtube_dl
from datetime import timedelta
from discord.ext import commands, tasks
from itertools import cycle
from random import choice, randint
from typing import Optional
from aiohttp import request
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown
from discord.ext.commands import has_permissions, MissingPermissions
from urllib import parse, request

bot = commands.Bot(command_prefix='::')
class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def avatar(self, ctx, member: discord.Member):
      await ctx.send("{}".format(member.avatar_url))

    @commands.command()
    async def add(self, ctx, left: int, right: int):
      await ctx.send(left + right)

    @commands.command()
    async def joined(self, ctx, member: discord.Member):
      await ctx.send(f'{member.name} joined in {member.joined_at}')

    @commands.command()
    async def apply(self, ctx):
        embed=discord.Embed(title="Staff Application", url="https://forms.gle/VJhGBbKUUQdbWBbq9", description="You can apply by clicking the title. Remember to be honest in you application.", color=0xFF5733)
        await ctx.send(embed=embed)

    @bot.command()
    async def whois(self, ctx, member:discord.Member =  None):

        if member is None:
            member = ctx.author
            roles = [role for role in ctx.author.roles]

        else:
            roles = [role for role in member.roles]

        embed = discord.Embed(title=f"{member}", color=0xff5917, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_author(name="User Info: ")
        embed.add_field(name="ID:", value=member.id, inline=False)
        embed.add_field(name="User Name:",value=member.display_name, inline=False)
        embed.add_field(name="Discriminator:",value=member.discriminator, inline=False)
        embed.add_field(name="Current Status:", value=str(member.status).title(), inline=False)
        embed.add_field(name="Current Activity:", value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "None", inline=False)
        embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
        embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
        embed.add_field(name=f"Roles [{len(roles)}]", value=" **|** ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Top Role:", value=member.top_role, inline=False)
        embed.add_field(name="Bot?:", value=member.bot, inline=False)
        await ctx.send(embed=embed)
        return

    class suggestions(commands.Cog):
        def __init__(bot):
            bot = bot

def setup(bot):
    bot.add_cog(Utility(bot))
