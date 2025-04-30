import discord
from discord.ext import commands
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()
TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    print("Error: TOKEN not found in .env file")
    exit()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

bot.run(TOKEN)