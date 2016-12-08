from os import path
from wordcloud import WordCloud, STOPWORDS
from bs4 import BeautifulSoup
import urllib2
import re

class WikiWordCloudGenerator(object):
    """Class that provided utilities to generate word clouds from Wikipedia URLs"""

    """generate a wordcloud image from a single wikipedia url"""
    def generate_wordcloud_from_url(self, wiki_url, image_output_file_name):
        raw_text = self.generate_text_from_url(wiki_url)
        self.generate_wordcloud_from_text(raw_text, image_output_file_name)

    """generate a wordcloud image from a string"""
    def generate_wordcloud_from_text(self, text_to_process, image_output_file_name):
        # Generate a word cloud image
        stopwords = set(STOPWORDS)
        stopwords.add("retrieved")
        wordcloud = WordCloud(stopwords=stopwords).generate(text_to_process)

        # Display the generated image:
        import matplotlib.pyplot as plt
        plt.imshow(wordcloud)
        plt.axis("off")
        if image_output_file_name:
            plt.savefig(image_output_file_name)
        else:
            plt.show()

    """generate a wordcloud image from a multiple wikipedia urls"""
    def generate_wordcloud_from_multiple_urls(self, wiki_urls, image_output_file_name):
        all_raw_text = []
        for url in wiki_urls:
            all_raw_text.append(self.generate_text_from_url(url))

        all_flattened = ''.join(all_raw_text)
        self.generate_wordcloud_from_text(all_flattened, image_output_file_name)

    """grabs text from a single url"""
    def generate_text_from_url(self, wiki_url):
        header = {'User-Agent': 'Mozilla/5.0'} # Needed to prevent 403 error on Wikipedia
        req = urllib2.Request(wiki_url,headers=header)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page)
        return soup.text