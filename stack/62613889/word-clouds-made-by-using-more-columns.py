import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

df = pd.DataFrame({'Date': ['01/01/2020', '01/01/2020', '01/01/2020', '01/01/2020', '01/01/2020', '01/02/2020', '01/02/2020'],
                   'Account': [412, 214, 53, 53, 214, 654, 41],
                   'Message': [np.NaN, np.NaN, "There are plenty of foods",
                               "'Now that we've fought off oxidative damage",
                               "Eggs are a very nutritious food",
                               "Unexplained cycle of AES is killing children",
                               "Green tea contains flavonoids"],
                   'Category': ['A', 'A', 'C', 'C', 'B', 'A', 'B']})
print(df)

stopwords = set[STOPWORDS]
def create_cloud(data, title = None):
    wordcloud = WordCloud(
        background_color='black',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40,
        scale=3,
        random_state=1
    ).generate(str(data))

    fig = plt.figure(1, figsize=(20, 20))
    plt.axis('off')
    if title:
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()

df.groupby('Date').apply(lambda x: create_cloud(x.Message.tolist()))