import requests

target_url = 'https://www.reddit.com/r/sports/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(target_url, headers=headers)

if response.status_code == 200:
    print(f"Successfully fetched the content from: {target_url}")
    html_content = response.text
    print("First 500 characters of the content:")
    print(html_content[:500])
else:
    print(f"Failed to fetch conctent. Status code: {response.status_code}")
