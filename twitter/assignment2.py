from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import json
import pandas as pd
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
from os import path
from PIL import Image

loc = path.dirname(__file__)
img = np.array(Image.open(path.join(loc, "test.png")))

ck = 'NwyXPX2muzzHHdPnmZoU0ME5O'
cs= 'OM6YrlNOfvZxE68vmMMNhVwXOov2XzaHqUFdE7jRI6taNIknQQ'
at = '226944425-hhIKArIDqj0id9QqhwhMLY7BGxQ2fAVTfczuBcsL'
ats = 'meFpmDmoMgjJGsK0pT37rpDvt4Ze3RODL7zavUbmWdyTD'

count = 20000
connect = OAuthHandler(ck, cs)
connect.set_access_token(at, ats)
api = API(connect, wait_on_rate_limit=True)

print("connection successful")

content = Cursor(api.search, q='makeinindia').items(count)

print("processing data....")
makeinindia = []
for i in content:
    makeinindia.append(json.loads(json.dumps(i._json)))
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'].encode('utf-8'), makeinindia)
text = " ".join(tweets['text'].values.astype(str))
final = " ".join([word for word in text.split()
                                if 'http' not in word and not word.startswith('@')and word != 'RT'])

print("creating word cloud....")

wc = WordCloud(background_color="black", max_words=1000)
wc.generate(final)
wc.to_file(path.join(loc, "test.png"))
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(img, cmap=plt.cm.gray)
plt.axis("off")
plt.show()