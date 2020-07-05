import numpy as np
import pandas as pd
import json
from tqdm import tqdm

with open('train-v2.0.json') as data_file:
    dataset = json.load(data_file)

js = pd.io.json.json_normalize(dataset, ['data','paragraphs','qas','answers'])
m = pd.io.json.json_normalize(dataset, ['data','paragraphs','qas'] )
r = pd.io.json.json_normalize(dataset, ['data','paragraphs'])
print(js.head())
print(m.head())
print(r.head())
