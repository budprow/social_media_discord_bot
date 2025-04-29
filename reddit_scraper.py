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
    print("\nBeautiful Soup object ceated.")

    # post_title_elements = soup.select('#main-content > div:nth-child(4) > shreddit-feed > article:nth-child(4)')
    # post_link_elements = soup.select_one('#post-title-t3_1k8shqj')

    # if len(post_title_elements) == len(post_link_elements):
    #     for i in range(len(post_title_elements)):
    #         title = post_title_elements[i].get_text(strip=True)
    #         link = post_link_elements[i]['href']
    #         if not link.startswith('http'):
    #             link = f'https://www.reddit.com{link}'

    feed = soup.find('shreddit-feed')
    if not feed:
        logging.error("Could not find the main feed container (<shreddit-feed>).")
        exit()

    post_element = feed.find('shreddit-post')
    
    if post_element:
        post_title = post_element.get('post-title', "Title not found")
        relative_link = post_element.get('permalink', None)

    if relative_link:
         post_link = f'https://www.reddit.com{relative_link}' if not relative_link.startswith('http') else relative_link
    else:
         post_link = "Link not found"

    title = post_title
    link = post_link

    print(f"Title: {title}")
    print(f"Link: {link}")
    print("------")

else:
        logging.warning("Could not find any <shreddit-post> element.")
    
# else:
#     print(f"Warning: Found {len(post_title)} titles and {len(link)} links. Counts may not match.")
    
    # else: print("Failed to fetch contenct. Status code: {response.status_code}")
