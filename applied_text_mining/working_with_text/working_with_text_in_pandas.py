import pandas as pd

time_sentences = ["Monday: The doctor's appointment is at 2:45pm.",
                  "Tuesday: The dentist's appointment is at 11:30 am.",
                  "Wednesday: At 7:00pm, there is a basketball game!",
                  "Thursday: Be back home by 11:15 pm at the latest.",
                  "Friday: Take the train at 08:10 am, arrive at 09:00am."]

df = pd.DataFrame(time_sentences, columns=['text'])
print(df)

# find the number of characters for each string in df['text']
print(df['text'].str.len())

# find the number of tokens for each string in df['text']
print(df['text'].str.split().str.len())

# find which entries contain the word 'appointment'
print(df['text'].str.contains('appointment'))

# find how many times a digit occurs in each string
print(df['text'].str.count(r'\d'))

# find all occurances of the digits
print(df['text'].str.findall(r'\d'))

# group and find the hours and minutes
print(df['text'].str.findall(r'(\d?\d):(\d\d)'))

# replace weekdays with '???'
print(df['text'].str.replace(r'\w+day\b', '???'))

# replace weekdays with 3 letter abbrevations
print(df['text'].str.replace(r'\w+day\b', lambda x: x[0][:3]))

# create new columns from first match of extracted groups
print(df['text'].str.extract(r'(\d?\d):(\d\d)'))

# extract the entire time, the hours, the minutes, and the period
print(df['text'].str.extractall(r'(\d?\d):(\d\d) ?([ap]m)'))

# extract the entire time, the hours, the minutes, and the period with group names
print(df['text'].str.extractall(r'(?P<time>(?P<hour>\d?\d):(?P<minute>\d\d) ?(?P<period>[ap]m))'))

