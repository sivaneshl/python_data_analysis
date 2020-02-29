text1 = "Ethics are built right into the ideals and objectives of the United Nations "
print(len(text1))

text2 = text1.split(' ') # Return a list of the words in text2, separating by ' '.
print(len(text2))

# List comprehension allows us to find specific words
# Words that are greater than 3 letters long in text2
print([w for w in text2 if len(w) > 3])
# Capitalized words in text2
print([w for w in text2 if w.istitle()])
# Words in text2 that end in 's'
print([w for w in text2 if w.endswith('s')])

# We can find unique words using set()
text3 = 'To be or not to be'
text4 = text3.split(' ')
print(len(set(text4)))
print(set(text4))
print(set(w.lower() for w in text4))

# Write code that would extract hashtags from the following tweet:
tweet = "@nltk Text analysis is awesome! #regex #pandas #python"
hashtags = [w for w in tweet.split(' ') if w.startswith('#')]
print(hashtags)


