import re

text5 = '"Ethics are built right into the ideals and objectives of the United Nations" \
#UNSG @ NY Society for Ethical Culture bit.ly/2guVelr @UN @UN_Women'
text6 = text5.split(' ')
print(text6)

# find hashtags
hashtags = [w for w in text5.split(' ') if w.startswith('#')]
print(hashtags)

# find callouts
callouts = [w for w in text5.split(' ') if w.startswith('@')]
print(callouts)
callouts = [w for w in text5.split(' ') if re.search('@[A-Za-z0-9_]+', w)]
print(callouts)
callouts = [w for w in text5.split(' ') if re.search('@\w+', w)]
print(callouts)

# finding specific characters
text12 = 'ouagadougou'
print(re.findall(r'[aeiou]', text12))
print(re.findall(r'[^aeiou]', text12))

# dates
datestr = '23-10-2002\n23/10/2002\n23/10/02\n10/23/2002\n23 Oct 2002\n23 October 2002\nOct 23, 2002\nOctober 23, 2002'
print(re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', datestr))
print(re.findall(r'\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{2,4}', datestr))
print(re.findall(r'(?:\d{1,2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (?:\d{1,2}, )?\d{2,4}', datestr))
