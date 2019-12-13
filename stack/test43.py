import pandas as pd
from nltk.chat.util import Chat, reflections

df = pd.DataFrame([['hello','Hi, How can i help you?'],
                   ['thanks','You are welcome'],
                   ['bye','Goodbye and have a nice day']],
                  columns=['Keywords','Answers'])

pairs = (df.set_index('Keywords')['Answers'].to_dict())

chat = Chat(pairs)
chat.converse()