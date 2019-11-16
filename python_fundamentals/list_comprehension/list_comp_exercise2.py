# Many organizations have user ids which are constrained in some way. Imagine you work at an internet service provider and the user ids are all two letters followed by two numbers (e.g. aa49). Your task at such an organization might be to hold a record on the billing activity for each possible user.
# Write an initialization line as a single list comprehension which creates a list of all possible user ids. Assume the letters are all lower case.

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [(a1 + a2 + n1 + n2) for a1 in lowercase for a2 in lowercase for n1 in digits for n2 in digits]
print(answer)
