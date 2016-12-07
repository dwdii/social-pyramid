from os import path
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import urllib2
import re

from WikiWordCloudGenerator import WikiWordCloudGenerator

generator = WikiWordCloudGenerator()

# example to generate from single url
#generator.generate_from_url("http://en.wikipedia.org/wiki/List_of_largest_corporate_profits_and_losses", "sampleout.png")

# example: generating from multiple urls
urls = ["http://en.wikipedia.org/wiki/Goldman_Sachs",
        "http://en.wikipedia.org/wiki/JPMorgan_Chase",
        "http://en.wikipedia.org/wiki/Morgan_Stanley",
        "http://en.wikipedia.org/wiki/Lehman_Brothers",
        "http://en.wikipedia.org/wiki/Financial_crisis_of_2007–2008"]

generator.generate_wordcloud_from_multiple_urls(urls, "financial_crisis.png")

# to generate the image inline, submit an empty string for the image filename
#generator.generate_wordcloud_from_multiple_urls(urls, "")
