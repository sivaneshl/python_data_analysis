import spacy
import pandas as pd
from difflib import SequenceMatcher
from spacy.lang.en import English

df = pd.DataFrame([[454232, 'Hi, first example 1'],
                   [321342, 'Now, second example'],
                   [412295, 'hello, a new example 1 in the third row'],
                   [432325, 'And now something completely different']],
                  columns=['Account', 'Message'])

test = 'Hi, first example 1'
df['r'] = df.apply(lambda x: SequenceMatcher(None, test, x.Message).ratio(), axis=1)
print(df)

spacyModel = spacy.load("en_core_web_sm")
# import en_core_web_sm
# spacyModel = en_core_web_sm.load()


list1 = ["Hi, first example 1"]
list2 = ["Now, second example","hello, a new example 1 in the third row","And now something completely different"]

list1SpacyDocs = [spacyModel(x) for x in list1]
list2SpacyDocs = [spacyModel(x) for x in list2]

similarityMatrix = [[x.similarity(y) for x in list1SpacyDocs] for y in list2SpacyDocs]

print(similarityMatrix)