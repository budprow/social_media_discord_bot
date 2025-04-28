import discord
from discord.ext import commands

TOKEN = ''

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