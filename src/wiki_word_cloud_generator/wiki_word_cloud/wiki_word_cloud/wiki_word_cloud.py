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
#urls = ["http://en.wikipedia.org/wiki/Goldman_Sachs",
        #"http://en.wikipedia.org/wiki/JPMorgan_Chase",
        #"http://en.wikipedia.org/wiki/Morgan_Stanley",
        #"http://en.wikipedia.org/wiki/Lehman_Brothers",
        #"http://en.wikipedia.org/wiki/Financial_crisis_of_2007–2008"]

#generator.generate_wordcloud_from_multiple_urls(urls, "financial_crisis.png")

# to generate the image inline, submit an empty string for the image filename
#generator.generate_wordcloud_from_multiple_urls(urls, "")

members_urls = ["http://en.wikipedia.org/wiki/Jeff_Sessions",
"http://en.wikipedia.org/wiki/James_Mattis",
"http://en.wikipedia.org/wiki/Tom_Price_(U.S._politician)",
"http://en.wikipedia.org/wiki/Ben_Carson",
"http://en.wikipedia.org/wiki/Betsy_DeVos",
"http://en.wikipedia.org/wiki/Nikki_Haley",
"http://en.wikipedia.org/wiki/Elaine_Chao",
"http://en.wikipedia.org/wiki/Steven_Mnuchin",
"http://en.wikipedia.org/wiki/Wilbur_Ross",
"http://en.wikipedia.org/wiki/Rex_Tillerson",
"http://en.wikipedia.org/wiki/Cathy_McMorris_Rodgers",
"http://en.wikipedia.org/wiki/Pete_Hegseth",
"http://en.wikipedia.org/wiki/Andrew_Puzder"
]

# generate word cloud for all cabinet members
generator.generate_wordcloud_from_multiple_urls(members_urls, "all_cabinet_members.png")

orgs_urls = [
"https://en.wikipedia.org/wiki/United_States_Congress",
"https://en.wikipedia.org/wiki/United_States_Central_Command",
"https://en.wikipedia.org/wiki/United_States_Congress",
"https://en.wikipedia.org/wiki/Johns_Hopkins_Hospital",
"https://en.wikipedia.org/wiki/Alliance_for_School_Choice",
"https://en.wikipedia.org/wiki/News_Corp",
"https://en.wikipedia.org/wiki/Invesco",
"https://en.wikipedia.org/wiki/ExxonMobil",
"https://en.wikipedia.org/wiki/Vets_For_Freedom",
"https://en.wikipedia.org/wiki/CKE_Restaurants"
]

# generate word cloud for all organizations that cabinet members are directly a part of (currently)
generator.generate_wordcloud_from_multiple_urls(orgs_urls, "all_cabinet_orgs.png")

# generate word cloud for all members AND all related orgs
generator.generate_wordcloud_from_multiple_urls(members_urls+orgs_urls, "all_cabinet_members_and_orgs.png")