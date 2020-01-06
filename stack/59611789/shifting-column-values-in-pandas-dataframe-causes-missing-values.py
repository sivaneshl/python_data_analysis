import pandas as pd
from io import StringIO


df = pd.DataFrame({'average_rating':['movie1', 'movie2', 'movie3', 'movie4', 'movie5'],
                   'isbn': [3.57, 3.60, 3.63, 3.98, 0.0],
                   'isbn13': ['0674842111', '1593600119', '156384155X', '1857237250', '0851742718'],
                   'language_code': ['978067', '978067', '978067', '978067', '978067'],
                   'num_pages': ['en-US', 'eng', 'eng', 'eng', 'eng'],
                   'ratings_count': [236, 400, 342, 383, 49],
                   'text_reviews_count': [55, 25, 38, 2197, 0],
                   'extra': [6.0, 4.0, 4.0, 17.0, 0.0]})

print(df)
df = df.astype(str)
df_shifted = (df.shift(-1,axis=1))
df_string = df_shifted.to_csv()
new_df = pd.read_csv(StringIO(df_string), index_col=0)
print(new_df)