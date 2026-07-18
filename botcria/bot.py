import discord
from discord.ext import commands
import asyncio
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
    await ctx.send("Eae seus comedia 🤖")
    await asyncio.sleep(2)
    await ctx.send("Tudo blz")

@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

bot.run(TOKEN)
