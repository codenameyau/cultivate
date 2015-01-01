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
    parser.add_argument('-l', default='jpn', help='language to learn')
    parser.add_argument('-t', default='eng', help='translated language')
    parser.add_argument('-n', type=int, default=0, help='sentence id')
    args = parser.parse_args()

    # Run scraper on tatoeba
    scrape = scraper.TatoebaScraper()
    scrape.set_languages(args.l, args.t)
    results = scrape.get_random_sentences(args.c)
    for i in range(len(results)):
        data = results[i]

        # Print sentence id
        lines = '-'*30
        print "\n%s\nTatoeba Sentence ID: %s\n%s\n" % (lines, data['sentence_id'], lines)

        # Print original sentence
        print data['original']['sentence']
        if 'romanization' in data['original']:
            print "%s" % data['original']['romanization']

        # Print translation
        if args.t in data['translations']:
            print "\n%s" % data['translations'][args.t]['sentence']
        else:
            print "\nTranslation for '%s' is not available." % args.t
        print ""

if __name__ == '__main__':
    main()
