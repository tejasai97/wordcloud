
from os import path

import also as also
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS


d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'pg4300.txt')).read()

# read the mask image
batman_mask = np.array(Image.open(path.join(d, "batman_mask.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")
stopwords.add("total")
stopwords.add("made")
stopwords.add("want")
stopwords.add("put")
stopwords.add("say")


wc = WordCloud(background_color="black", max_words=2000, mask=batman_mask,
               stopwords=stopwords)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "result.png"))

# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(batman_mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()