import discord
import random
import asyncio
from discord import Member, Embed
from typing import Optional
from discord.ext import commands
from discord.ext.commands import BadArgument

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
      await ctx.send("Pong!")

    @commands.command(pass_context=True)
    async def punch(self, ctx, member: discord.Member):
      """Punch someone."""
      embed = discord.Embed(title="Kapow!", description="**{1}** punches **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
      embed.set_thumbnail(url="https://m.popkey.co/7bc81e/vzaX9_s-200x150.gif")
      await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def shoot(self, ctx, member: discord.Member):
      """Shoot someone."""
      embed = discord.Embed(title="Pow Pow Pow!", description="**{1}** shoots **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
      embed.set_thumbnail(url="https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif")
      await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def cookie(self, ctx, member: discord.Member):
      """Give a cookie to someone."""
      embed = discord.Embed(title="Nom nom nom!", description="**{1}** gave a cookie to **{0}**! :cookie:".format(member.name, ctx.message.author.name), color=0x176cd5)
      await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def hug(self, ctx, member: discord.Member):
      """Hug someone."""
      embed = discord.Embed(title="Huggies!", description="**{1}** hugs **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
      embed.set_thumbnail(url="https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif?itemid=7939558")
      await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def slots(self, ctx):
      """Play a very basic version of slots."""
      responses = ["🍋" , "🍊", "🍉", ":seven:", ]
      embed=discord.Embed(title="🎰 Slot Machine 🎰", description=random.choice(responses) + random.choice(responses) + random.choice(responses), color=0x176cd5)
      embed.set_footer(text="You need triple 7's to win.")
      await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def hello(self, ctx):
      await ctx.send("Hello!")

    @commands.command()
    async def eightball(self, ctx):
      choices = ["I believe so,", "Why not", "Pretty sure not,", "I agree", "I disagree", "Of course"]
      await ctx.send(random.choice(choices))

    @commands.command()
    async def coinflip(self, ctx):
      choices = ["Heads", "Tails"]
      await ctx.send(random.choice(choices))

    @commands.command()
    async def gayrate(self, ctx):
      percentage = (random.randint(0, 100))
      await ctx.send(f'You are {percentage}% gay :rainbow_flag:')

    @commands.command()
    async def simprate(self, ctx):
      percentage = (random.randint(0, 100))
      await ctx.send(f'You are {percentage}% a simp')
      
    @commands.command()
    async def say(self, ctx, arg):
      await ctx.send(arg)

    @commands.command()
    async def owo(self, ctx):
      await ctx.send('OwO')

    @commands.command()
    async def slap(self, ctx, member: Member, *, reason: Optional[str] = "for no reason"):
	    await ctx.send(f"{ctx.author.display_name} slapped {member.mention} {reason}!")

    @slap.error
    async def slap_error(self, ctx, exc):
	    if isinstance(exc, BadArgument):
		    await ctx.send("'I can't find that member.'")

    @commands.command()
    async def meme(self, ctx):
        memes = [
            "https://cdn.discordapp.com/attachments/471397786613579777/584150839669817344/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/584054714925187072/byemom.png",
            "https://cdn.discordapp.com/attachments/471397786613579777/584013133606027286/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/584012903749779456/2pYlD19.png",
            "https://cdn.discordapp.com/attachments/471397786613579777/583698535938129929/image0.png",
            "https://cdn.discordapp.com/attachments/471397786613579777/583486555990130688/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/583480637713940480/image0.png",
            "https://cdn.discordapp.com/attachments/471397786613579777/583474303975161857/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/583470910644682752/eyes.png",
            "https://cdn.discordapp.com/attachments/471397786613579777/583061107359612981/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/583043410370494499/unknown.png",
            "https://cdn.discordapp.com/attachments/471397786613579777/583042920047706122/wtf.png",
            "https://cdn.discordapp.com/attachments/471397786613579777/582702902192111666/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/582704640597032990/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/582698036203880459/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/582697670825476116/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/582691116621496350/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/582467755052367872/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/582226635701354516/Untitled7.png",
            "https://cdn.discordapp.com/attachments/471397786613579777/582161702553124864/image0.jpg",
            "https://cdn.discordapp.com/attachments/471397786613579777/581168117754101761/IMG_20190523_181356.png",
            "https://cdn.discordapp.com/attachments/471397786613579777/581081119076646912/image0-21-1-2-1.png",
            "https://cdn.discordapp.com/attachments/471397786613579777/580481784802967562/image0.jpg","https://cdn.discordapp.com/attachments/777949719154524190/819951085422247997/20200129_085917.jpg","https://cdn.discordapp.com/attachments/777949719154524190/809127010446082068/video0.mp4","https://cdn.discordapp.com/attachments/788937904859906068/803841355951505408/video0-14.mp4","https://cdn.discordapp.com/attachments/788937904859906068/803840924291170304/ravens_ashtray_20210119_3.mp4","https://cdn.discordapp.com/attachments/777949719154524190/803517800039317564/video0.mp4","https://cdn.discordapp.com/attachments/755024333138821191/799316503958257674/arMeRM7_460sv.mp4","https://cdn.discordapp.com/attachments/755024333138821191/799313938764136498/video0_2.mp4","https://cdn.discordapp.com/attachments/755024333138821191/799315154017189938/video0_7.mp4","https://cdn.discordapp.com/attachments/776596371150209027/830095969219117076/I_said_some.png","https://cdn.discordapp.com/attachments/776596371150209027/830608755002441738/images.png","https://cdn.discordapp.com/attachments/776596371150209027/830609040757096469/images.png","https://cdn.discordapp.com/attachments/776596371150209027/830609896893579315/4pc77e.png"
        ]
        await ctx.send(f"meme: {random.choice(memes)}")

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def kill(self, ctx, member : discord.Member):
      muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
      await ctx.message.delete()
      await member.add_roles(muted_role)
      embed = discord.Embed(description= f"**{member.display_name}#{member.discriminator} was killed**", color=discord.Color.green())
      await ctx.send(embed=embed)
      await asyncio.sleep(60.0)
      await member.remove_roles(muted_role)

    @commands.command()
    async def penis(self, ctx, user : discord.Member):
        """Detects user's penis length
        This is 100% accurate."""
        random.seed(user.id)
        p = "8" + "="*random.randint(0, 10) + "D"
        await ctx.send("Size: " + p)

def setup(bot):
    bot.add_cog(Fun(bot))
