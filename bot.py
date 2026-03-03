import discord
import os
from bot_mantik import yazi_tura, gen_pass,saatsoyle 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$sifre'):
        await message.channel.send("Sifreniz: " + gen_pass(10))
    elif message.content.startswith('$oyun'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('$saat'):
        await message.channel.send("su anda saat:"+saatsoyle())
    else:
        await message.channel.send(message.content)

client.run(TOKEN)