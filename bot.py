import discord
from discord.ext import commands, tasks
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv # type: ignore
import logging
import json

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
sent_posts_file = 'sent_posts.json'

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

async def load_sent_posts():
    try:
        with open(sent_posts_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from {sent_posts_file}. Starting with an empty list.")
        return []

async def save_sent_posts(sent_posts):
    with open(sent_posts_file, 'w') as f:
        json.dump(sent_posts, f, indent=4)

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
        sent_posts = await load_sent_posts()
        new_posts_to_send = []
        for post in posts:
            new_posts_to_send.append(post)
            sent_posts.append(post['link'])

        channel = bot.get_channel(notification_channel_id)
        if channel:
            for post in new_posts_to_send:
                embed = discord.Embed(title=post['title'], url=post['link'])
                await channel.send(embed=embed)
            await save_sent_posts(sent_posts)
        else:
            logging.error(f"Could not find the notification channel with ID: {notification_channel_id}")

@scrape_reddit.before_loop
async def before_scrape_reddit():
    await bot.wait_until_ready()

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

bot.run(TOKEN)