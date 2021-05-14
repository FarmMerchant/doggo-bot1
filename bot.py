import discord
import nacl
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
bot.remove_command('help')
status = cycle(['::help for help!', '::botinfo for info!'])
extension = ".py"


@bot.event
async def on_ready():
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print("Logged in as")
	print("Username: %s" % bot.user.name)
	print("ID: %s" % bot.user.id)
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	change_status.start()\


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')


@tasks.loop(seconds=10)
async def change_status():
	await bot.change_presence(activity=discord.Game(next(status)))


my_secret = os.environ['TOKEN']
bot.run(os.getenv('TOKEN'))
