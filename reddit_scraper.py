import requests
from bs4 import BeautifulSoup

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

    post_title_elements = soup.select('a > faceplate-screen-reader-content')
    post_link_elements = soup.select_one('a[slot="full-post-link"]')

    if len(post_title_elements) == len(post_link_elements):
        for i in range(len(post_title_elements)):
            title = post_title_elements[i].get_text(strip=True)
            link = post_link_elements[i]['href']
            if not link.startswith('http'):
                link = f'https://www.reddit.com{link}'
            print(f"Title: {title}")
            print(f"Link: {link}")
            print("------")

    else:
        print(f"Warning: Found {len(post_title_elements)} titles and {len(post_link_elements)} links. Counts may not match.")

else: print("Failed to fetch contenct. Status code: {response.status_code}")
