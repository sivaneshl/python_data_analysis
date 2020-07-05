import pandas as pd
from nltk import everygrams, word_tokenize, FreqDist
import string

df = pd.DataFrame({'open_answers' : ['With this script, I get a table with all the words that occur to look instead of I know.',
                                     'With this, But, I also want to look this for combinations script of words this I know.',
                                     'For example, I know that the combination of different and employees seperately instead of in combination.']})

df['combinations'] = df['open_answers']\
    .apply(lambda x: [' '.join(word) for word in everygrams(word_tokenize(x.translate(str.maketrans('', '', string.punctuation))), 2, 2)])

result = pd.DataFrame(list(FreqDist([''.join(y) for x in df['combinations'] for y in x]).items()), columns=['combination', 'freq'])
print(result)


# df['open_answers']=df['open_answers'].apply(lambda x: ' '.join([item for item in x.split()]))
# sequence_of_sentences=df['open_answers']
# from collections import Counter
# counts=Counter()
# for sentence in sequence_of_sentences:
#    counts.update(word.strip('.,?!"\"').lower() for word in sentence.split())
#
# df1=(df['open_answers'].str.split(expand=True)
#         .stack()
#         .value_counts()
#         .rename_axis('word')
#         .reset_index(name='frequency'))
# print(df1)