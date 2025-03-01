import requests
from bs4 import BeautifulSoup
from newspaper import Article
import json

urls = {
    "Wikipedia": "https://en.wikipedia.org/wiki/Cybersecurity",
    "OWASP Top 10": "https://owasp.org/www-project-top-ten/",
    "NIST Cybersecurity": "https://www.nist.gov/cyberframework"
}

def scrape_wikipedia(url):
    """Scrape Wikipedia articles and extracts main content."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    paragraphs = soup.find_all('p')
    text = "\n".join([para.get_text() for para in paragraphs])
    return text.strip()

def scrape_article(url):
    """Scrape news articles and extracts main content."""
    article = Article(url)
    article.download()
    article.parse()
    return article.text.strip()

def scrape_data():
    """Scrape data from various sources."""
    data = {}
    for site, url in urls.items():
        print(f"Scraping {site}...")
        try:
            if "wikipedia.org" in url:
                content = scrape_wikipedia(url)

            else:
                content = scrape_article(url)
            data[site] = content
        except Exception as e:
            print(f"Failed to scrape {site}: {e}")
        
    # Save to JSON
    with open("cs_data.json","w",encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)
    print("Data saved to cs_data.json")

scrape_data()