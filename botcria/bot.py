import discord

from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="@", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} está online!")

@bot.command()
async def oi(ctx):
    await ctx.send("Olá! Estou funcionando 🤖")
    await asyncio.sleep(2)
    await ctx.send("O que deseja?")

@bot.command()
async def tocar(ctx):

    if ctx.author.voice is None:
        await ctx.send("Você precisa estar em call jumento")
        return

    # pega a call onde o usuária ta
    call = ctx.author.voice.channel

    # bot entra na call
    voz = await call.connect()

    sirius = "musica.py"

voz.play(discord.FFmpegPCMAudio(sirius))

    await ctx.send("Música tocando")

bot.run(TOKEN)
