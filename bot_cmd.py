import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from bot_mantik import yazi_tura, gen_pass,saatsoyle 


load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def saat(ctx):
    await ctx.send("saat su anda tam olarak " + saatsoyle())

@bot.command()
async def oyun(ctx):
    await ctx.send(yazi_tura())

@bot.command()
async def sifre(ctx):
    await ctx.send("sifreniz: "+ gen_pass(10))

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name}, {discord.utils.format_dt(member.joined_at)}\'de katildi')




bot.run(TOKEN)