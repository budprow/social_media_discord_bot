import requests
from bs4 import BeautifulSoup
import logging

target_url = 'https://www.reddit.com/r/sports/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(target_url, headers=headers)

if response.status_code == 200:
    print(f"Successfully fetched the content from: {target_url}")
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    print("\nBeautiful Soup object created.")

    feed = soup.find('shreddit-feed')
    if not feed:
        logging.error("Could not find the main feed container (<shreddit-feed>).")
        exit()

    post_elements = feed.find_all('shreddit-post')

    if post_elements:
        print("\nFound the following post titles and links:")
        for post_element in post_elements:
            post_title = post_element.get('post-title', "Title not found")
            relative_link = post_element.get('permalink', None)

            if relative_link:
                post_link = f'https://www.reddit.com{relative_link}' if not relative_link.startswith('http') else relative_link
            else:
                post_link = "Link not found"

            print(f"Title: {post_title}")
            print(f"Link: {post_link}")
            print("------")
    else:
        logging.warning("Could not find any <shreddit-post> elements.")

else:
    print(f"Failed to fetch content. Status code: {response.status_code}")
