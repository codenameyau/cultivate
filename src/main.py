"""
Cultivate - main.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
from tatoeba import scraper

def main():
    s = scraper.TatoebaScraper()
    s.set_url('http://tatoeba.org/eng/sentences/show/94899')
    s.get_random_sentence()

if __name__ == '__main__':
    main()
