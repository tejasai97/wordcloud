
from os import path

import also as also
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS


loc = path.dirname(__file__)


text = open(path.join(loc, 'pg4300.txt')).read()


img = np.array(Image.open(path.join(loc, "mj.png")))

stop = set(STOPWORDS)

test = WordCloud(background_color="black", max_words=600, mask=img,
               stopwords=stop)

test.generate(text)

test.to_file(path.join(loc, "show.png"))


plt.imshow(test)
plt.axis("off")
plt.figure()
plt.imshow(img, cmap=plt.cm.gray)
plt.axis("off")
plt.show()