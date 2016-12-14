try:
    import nltk
    from nltk.corpus import stopwords
except:
    print 'import nltk error'
import string
import pandas as pd
import pylab
import matplotlib.pyplot as plt
from WikiWordCloudGenerator import WikiWordCloudGenerator

generator = WikiWordCloudGenerator()

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


# clean up wiki scraped text
wiki_raw = generator.get_combined_scraped_text(members_urls)
wiki_raw = ''.join([i for i in wiki_raw if not i.isdigit()])
wiki_raw = ''.join([i if ord(i) < 128 else '' for i in wiki_raw])
wiki_raw = wiki_raw.encode("utf-8").split()
s=set(stopwords.words('english'))
s.add('retrieved')
wiki_raw = filter(lambda w: not w in s, wiki_raw)

wiki_unique = set()
wiki_all_filtered = []
enoding_errors = []
table = string.maketrans("","")
def trans_punc(s):
    return s.translate(table, string.punctuation)
for w in wiki_raw:
    try:
        trans = trans_punc(str(w.lower()))
        # filter out empty strings
        if trans:
            wiki_unique.add(trans)
            wiki_all_filtered.append(trans)
    except Exception:
        pass

print('Total Number of Words: %i' % len(wiki_all_filtered))

print('Number of Unique Words: %i' % len(wiki_unique))

fd = nltk.FreqDist([w.lower() for w in wiki_all_filtered])

# translate results into pandas dataframe
wiki_df = pd.DataFrame(fd.items(), columns=['Word', 'Frequency'])
wiki_df = wiki_df.sort(['Frequency'], ascending=[0])

# plot top 200 words frequency
plt.title("Distribution of words")
plt.plot(list(wiki_df['Frequency']))
plt.savefig('zipf.png')
plt.clf()

wiki_df['CummSum'] = wiki_df['Frequency'].cumsum()
wiki_df['GtHalf'] = wiki_df['CummSum'] > (len(wiki_all_filtered) / 2.0)
wiki_df.index = range(1,len(wiki_df) + 1)

print wiki_df

# find how many words sum to be half of the total words
half_point = wiki_df['GtHalf'] == True
print wiki_df[half_point].head(1)

# show zipf trend
plt.title("Distribution of words (Loglog)")
plt.loglog(wiki_df.index,wiki_df['Frequency'])
plt.savefig('zipf_loglog.png')