"""
Cultivate - scraper.py
Apache License (c) 2015
https://github.com/codenameyau/cultivate
"""
import requests
import bs4

class TatoebaScraper:

    def __init__(self):
        """
        Constructor: (String, String) -> TatoebaScraper
        Sets up the class data structures
        """
        # Define language settings
        self.language_original = 'jpn'
        self.language_translated = 'eng'
        self.supported_languages = (
            'cmn',  # Chinese
            'deu',  # German
            'eng',  # English
            'fin',  # Finnish
            'fra',  # French
            'ita',  # Italian
            'jpn',  # Japanese
            'kor',  # Korean
            'pol',  # Polish
            'por',  # Portuguese
            'rus',  # Russian
            'spa',  # Spanish
        )

        # Define site path to scrape random sentence
        self.site_base = 'http://tatoeba.org/eng/sentences/show/'
        self.site_url = self.site_base + self.language_original
        self.sentences = []
        self.soup = None


    ##################
    # Public Methods #
    ##################
    def set_languages(self, original, translated):
        """
        Public: (String, String) -> None
        Sets the languages for the scraper
        """
        if translated in self.supported_languages \
            and original in self.supported_languages:
            self.language_translated = translated
            self.language_original = original
            self.set_url(self.language_original)

    def set_url(self, target):
        """
        Public: (String) -> None
        Sets the site_url to specified url
        """
        self.site_url = self.site_base + target

    def scrape_sentence(self, res):
        """
        Public: (Response) -> String
        Returns the scraped content from response
        """
        data = {}
        if res.status_code == 200:
            self.soup = bs4.BeautifulSoup(res.content)
            self._find_sentence_id(data)
            self._find_original_sentence(data)
            self._find_translations(data)
        return data

    def get_random_sentences(self, count):
        """
        Public: (Int) -> String
        Scrapes the site and finds target article
        """
        for i in range(0, count):
            scraped = self.scrape_sentence(requests.get(self.site_url))
            if scraped:
                self.sentences.append(scraped)
        return self.sentences

    def get_sentence_by_id(self, sentence_id):
        """
        Public: (Int) -> String
        Returns the scraped sentence by the given id
        """
        self.set_url(str(sentence_id))
        scraped = self.scrape_sentence(requests.get(self.site_url))
        if scraped:
            self.sentences.append(scraped)
        return self.sentences


    ####################
    # Internal Methods #
    ####################
    def _find_sentence_id(self, data):
        """
        Internal: None -> None
        Stores the sentence id into data
        """
        data['sentence_id'] = self.soup.find(id='SentenceSentenceId').attrs['value']

    def _add_romanization(self, div, data):
        """
        Internal: (Tag, Dict) -> None
        """
        romanization = div.find('div', class_='romanization')
        if romanization:
            if 'title' in romanization.attrs:
                data['romanization'] = romanization.attrs['title']

    def _find_original_sentence(self, data):
        """
        Internal: (Dict) -> None
        Stores the main sentence into data
        """
        div = self.soup.find('div', class_='mainSentence')
        data['original'] = {}
        data['original']['sentence'] = div.find('div', class_='text').string
        self._add_romanization(div, data['original'])

    def _find_translations(self, data):
        """
        Internal: (Dict) -> None
        Finds all additional translations and store in data
        """
        # [TODO]: Add romanization other languages
        data['translations'] = {}

        # Scrape alt flag name and translation text
        div = self.soup.find('div', class_='translations')
        translations = div.find_all('a', class_='text')
        flags = div.find_all('img', class_='languageFlag')
        for i in range(0, len(translations)):
            lang_short = flags[i].attrs['alt']
            data['translations'][lang_short] = {
                'sentence': translations[i].string,
                'language': flags[i].attrs['title'],
                }
