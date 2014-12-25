"""
Cultivate - main.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
from tatoeba import scraper
import argparse

def main():
    """
    Runs main program to parse arguments and retrieve
    random sentences from tatoeba.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Select languages and sentences')
    parser.add_argument('-c', type=int, default=1, help='count')
    parser.add_argument('-o', default='jpn', help='original language')
    parser.add_argument('-t', default='eng', help='translated language')
    args = parser.parse_args()

    # Run scraper on tatoeba
    scrape = scraper.TatoebaScraper()
    scrape.set_languages(args.o, args.t)
    results = scrape.get_random_sentences(args.c)
    for i in range(len(results)):
        print results[i]
        print

if __name__ == '__main__':
    main()
