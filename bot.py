import discord
import random
import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(command_prefix='::')
bot.remove_command('help')

@bot.command(pass_context=True)
async def info(ctx):
    embed=discord.Embed(title="Doggo Bot", description="Doggo Bot is currently being worked on.", color=0xff5917)
    embed.add_field(name="**Creation Date**", value="`Doggo Bot was made on April 3, 2021`", inline=False)
    embed.add_field(name="Command Prefix", value="`::`", inline=False)
    embed.set_footer(text="Created by Farm Merchant#9926")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def eightball(ctx):
    choices = ["I believe so,", "Why not", "Pretty sure not,", "I agree", "I disagree", "Of course"]
    await ctx.send(random.choice(choices))

@bot.command()
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    await ctx.send(random.choice(choices))

@bot.command()
async def gayrate(ctx):
    percentage = (random.randint(0, 100))
    await ctx.send(f'You are {percentage}% gay :rainbow_flag:')

@bot.command()
async def simprate(ctx):
    percentage = (random.randint(0, 100))
    await ctx.send(f'You are {percentage}% a simp')

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name='::help for help!'))
  print('Bot is ready')

@bot.command()
async def serverip(ctx):
    await ctx.send('The server ip is DoggoBox.minehut.gg')

@bot.group(name='help', invoke_without_command=True)
async def help(ctx):
    embed=discord.Embed(title="", description="**List of Commands.**", color=0xff5917)
    embed.set_author(name="Doggo Bot Commands",icon_url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
    embed.add_field(name=":sparkles:**Fun Commands**", value="`::help fun`", inline=True)
    embed.add_field(name=":question:**Info Commands**", value="`::help commands`", inline=True)
    embed.add_field(name=":question:**Info Commands**", value="`info, commands`", inline=True)
    embed.set_footer(text="Created by Farm Merchant#9926")
    await ctx.send(embed=embed)

@help.command(name='misc')
async def misc_subcommand(ctx):
  await ctx.channel.send("Misc")

keep_alive()
bot.run(os.getenv('TOKEN'))
