"""
Cultivate - main.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
from tatoeba import scraper

def main():
    """
    Runs main program to parse arguments and retrieve
    random sentences from tatoeba.
    """
    scrape = scraper.TatoebaScraper()
    results = scrape.get_random_sentences(1)
    for i in range(len(results)):
        print results[i]
        print

if __name__ == '__main__':
    main()
