import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq(hl='en-AU', tz=360)
# keywords = pd.read_csv("keywordlist.txt")
keywords = ['python', 'django', 'go', 'jaahfhaj']

pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     geo='AU',
     gprop='')
data = pytrend.interest_over_time()
data.to_csv('KeywordList.csv', encoding='utf_8_sig')