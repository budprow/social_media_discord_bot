import discord
from discord.ext import commands, tasks
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv # type: ignore
import logging

load_dotenv()
TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    print("Error: TOKEN not found in .env file")
    exit()
target_reddit_url = 'https://www.reddit.com/r/sports/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
notification_channel_id = 1365777106277105717

intents = discord.Intents.default()
# intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

async def get_reddit_posts():
    try:
        response = requests.get(target_reddit_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        feed = soup.find('shreddit-feed')
        if not feed:
            logging.error("Could not find the main feed container (<shreddit-feed>).")
            return []
        post_elements = feed.find_all('shreddit-post')
        posts = []
        for post_element in post_elements:
            title = post_element.get('post-title', "Title not found")
            relative_link = post_element.get('permalink', None)
            if relative_link:
                link = f'https://www.reddit.com{relative_link}' if not relative_link.startswith('http') else relative_link
            else:
                link = "Link not found"
            posts.append({'title': title, 'link': link})
        return posts
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Reddit posts: {e}")
        return []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')
    scrape_reddit.start()

@tasks.loop(minutes=1)
async def scrape_reddit():
    posts = await get_reddit_posts()
    if posts:
        channel = bot.get_channel(notification_channel_id)
        if channel:
            for post in posts:
                embed = discord.Embed(title=post['title'], url=post['link'])
                await channel.send(embed=embed)

@scrape_reddit.before_loop
async def before_scrape_reddit():
    await bot.wait_until_ready()

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

bot.run(TOKEN)