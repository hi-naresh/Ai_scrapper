import json
from scrapy.crawler import CrawlerProcess
from activity_spider import ActivitySpider

from dumper import save_data
from processor import process_text
from search import search_for_websites

# python -m spacy download en_core_web_sm
# Load SpaCy for NLP tasks
# nlp = spacy.load("en_core_web_sm")

# Keywords for search
keywords = ["mental", "physical", "activities"]

# Main scraping function
def main():
    # Search for websites
    urls = search_for_websites(keywords)
    print(f"Found URLs: {urls}")

    # Scrape data from websites
    process = CrawlerProcess()
    process.crawl(ActivitySpider, start_urls=urls)
    process.start()

    # Load scraped data
    with open('activities.json', 'r') as f:
        data = json.load(f)

    # Process text using NLP
    for key, value in data.items():
        data[key] = process_text(value)

    # Save data
    save_data(data)
    
if __name__ == '__main__':
    main()
