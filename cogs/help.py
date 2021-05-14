import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='help', invoke_without_command=True)
    async def help(self, ctx):
      embed=discord.Embed(title="", description="**List of Commands.**", color=0xff5917)
      embed.set_author(name="Doggo Commands",icon_url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.set_thumbnail(url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.add_field(name="`Fun Commands`", value="::help fun", inline=True)
      embed.add_field(name="`Utility Commands`", value="::help utility", inline=True)
      embed.add_field(name="`Info Commands`", value="::help info", inline=True)
      embed.add_field(name="`Mod Commands`", value="::help mod", inline=True)
      embed.add_field(name="`Music Commands`", value="::help music", inline=True)
      embed.set_footer(text="Created by Farm Merchant#9926")
      await ctx.send(embed=embed)

    @help.command(name='fun')
    async def fun_subcommand(self, ctx):
      embed=discord.Embed(title="", description=":sparkles:**Fun Commands**:sparkles:", color=0xff5917)
      embed.set_author(name="Doggo Commands",icon_url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.set_thumbnail(url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.add_field(name="`::hello`", value="Hello!", inline=False)
      embed.add_field(name="`::coinflip [question]`", value="Flips a coin.", inline=False)
      embed.add_field(name="`::simprate`", value="Are you a simp?", inline=False)
      embed.add_field(name="`::gayrate`", value="How gay are you?", inline=False)
      embed.add_field(name="`::eightball`", value="Rolls an eightball.", inline=False)
      embed.add_field(name="`::ping`", value="Pong!", inline=False)
      embed.add_field(name="`::say (message)`", value="Repeats your message.", inline=False)
      embed.add_field(name="`::owo`", value="OwO.", inline=False)
      embed.add_field(name="`::slap (member) (reason)`", value="Slaps them.", inline=False)
      embed.add_field(name="`::penis (member)`", value="Measures your coc.", inline=False)
      embed.set_footer(text="Created by Farm Merchant#9926", icon_url="https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/cd/Wooden_Hoe_JE3_BE3.png/revision/latest/scale-to-width-down/150?cb=20200226194121")
      await ctx.send(embed=embed)

    @help.command(name='info')
    async def info_subcommand(self, ctx):
      embed=discord.Embed(title="", description=":question:**Info Commands**:question:", color=0xff5917)
      embed.set_author(name="Doggo Commands", icon_url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.set_thumbnail(url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.add_field(name="`::botinfo`", value="Shows information about this bot.", inline=False)
      embed.add_field(name="`::serverinfo`", value="Shows information about this bot.", inline=False)
      embed.add_field(name="`::whois (member)`", value="Shows info about the member.", inline=False)
      embed.set_footer(text="Created by Farm Merchant#9926", icon_url="https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/cd/Wooden_Hoe_JE3_BE3.png/revision/latest/scale-to-width-down/150?cb=20200226194121")
      await ctx.send(embed=embed)

    @help.command(name='utility')
    async def utility_subcommand(self, ctx):
      embed=discord.Embed(title="", description=":wrench:**Utility Commands**:wrench:", color=0xff5917)
      embed.set_author(name="Doggo Commands",icon_url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.set_thumbnail(url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.add_field(name="`::add (number) (number)`", value="Adds numbers together.", inline=False)
      embed.add_field(name="`::avatar (member)`", value="Shows you someones avatar.", inline=False)
      embed.add_field(name="`::joined (member)`", value="When a user joined.", inline=False)
      embed.set_footer(text="Created by Farm Merchant#9926", icon_url="https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/cd/Wooden_Hoe_JE3_BE3.png/revision/latest/scale-to-width-down/150?cb=20200226194121")
      await ctx.send(embed=embed)

    @help.command(name='mod')
    @commands.has_permissions(administrator=True)
    async def mod_subcommand(self, ctx):
      embed=discord.Embed(title="", description=":key:**Mod Commands**:key:", color=0xff5917)
      embed.set_author(name="Doggo Commands",icon_url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.set_thumbnail(url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.add_field(name="`::ban (member) (reason)`", value="Bans member.", inline=False)
      embed.add_field(name="`::unban (member)`", value="Unbans member.", inline=False)
      embed.add_field(name="`::kick (member) (reason)`", value="Kick member.", inline=False)
      embed.add_field(name="`::mute (member) (reason)`", value="Mutes member.", inline=False)
      embed.add_field(name="`::unmute (member)`", value="Unmutes member.", inline=False)
      embed.add_field(name="`::tempmute (member) (time(s, m, h, d))`", value="Temporarily mutes member.", inline=False)
      embed.add_field(name="`::lock`", value="Lock the channel.", inline=False)
      embed.add_field(name="`::unlock`", value="Unlock the channel.", inline=False)
      embed.add_field(name="`::clear (number)`", value="Clears a number of messages.", inline=False)
      embed.add_field(name="`::clearchannel`", value="Clear the channels messages.", inline=False)
      embed.add_field(name="`::warn (member) (reason)`", value="Warns the member.", inline=False)
      embed.add_field(name="`::warnings (member)`", value="Shows the warnings the user has.", inline=False)
      embed.set_footer(text="Created by Farm Merchant#9926", icon_url="https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/cd/Wooden_Hoe_JE3_BE3.png/revision/latest/scale-to-width-down/150?cb=20200226194121")
      await ctx.send(embed=embed)

    @help.command(name='music')
    async def music_subcommand(self, ctx):
      embed=discord.Embed(title="", description=":musical_note: **Mod Commands**:musical_note: ", color=0xff5917)
      embed.set_author(name="Doggo Commands",icon_url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.set_thumbnail(url="https://i.pinimg.com/originals/0c/6e/aa/0c6eaafb54d1f06186206e3f252587cf.gif")
      embed.add_field(name="`::play (youtube url)`", value="Plays song.", inline=False)
      embed.add_field(name="`::pause`", value="Pauses music.", inline=False)
      embed.add_field(name="`::resume`", value="Resumes music.", inline=False)
      embed.add_field(name="`::stop`", value="Clears the queue and leaves the voice channel.", inline=False)
      embed.add_field(name="`::leave`", value="Clears the queue and leaves the voice channel.", inline=False)
      embed.add_field(name="`::now`", value="Displays the currently playing song.", inline=False)
      embed.add_field(name="`::skip`", value="Vote to skip a song. The requester can automatically skip. 3 skip votes are needed for the song to be skipped", inline=False)
      embed.add_field(name="`::queue`", value="Shows the player's queue.", inline=False)
      embed.add_field(name="`::shuffle`", value="Shuffles the queue.", inline=False)
      embed.add_field(name="`::remove (number) `", value="Removes a song from the queue at a given index.", inline=False)
      embed.add_field(name="`::loop`", value="Loops the currently playing song (BROKEN)", inline=False)
      embed.set_footer(text="Created by Farm Merchant#9926", icon_url="https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/cd/Wooden_Hoe_JE3_BE3.png/revision/latest/scale-to-width-down/150?cb=20200226194121")
      await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
