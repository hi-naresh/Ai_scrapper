import requests
from bs4 import BeautifulSoup

def search_for_websites(keywords):
    found_urls = []
    for keyword in keywords:
        query = '+'.join(keyword.split())
        url = f"https://www.google.com/search?q={query}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        proxies = {
            'http': 'http://10.10.1.10:3128',
            'https': 'http://10.10.1.10:1080',
        }
        # response = requests.get(url, headers=headers)
        response = requests.get(url, headers=headers, proxies=proxies)

        if response.status_code != 200:
            print(f"Failed to fetch page, status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"HTML output for keyword '{keyword}': {soup.prettify()[:1000]}")  # Print first 1000 chars of HTML

        for link in soup.find_all('a', href=True):
            href = link['href']
            if '/url?q=' in href:
                clean_url = href.split('/url?q=')[1].split('&')[0]
                if clean_url.startswith("http"):
                    found_urls.append(clean_url)
                    if len(found_urls) >= 2:
                        break
    return found_urls
