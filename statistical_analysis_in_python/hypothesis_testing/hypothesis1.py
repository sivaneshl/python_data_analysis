import pandas as pd
from scipy import stats


df = pd.read_csv('C:/python_data_analysis/resources/course1_downloads/grades.csv')
print(len(df))
print(df.head())

early = df[df['assignment1_submission'] <= '2015-31-12']
late = df[df['assignment1_submission'] > '2015-31-12']

print(early.mean())
print(late.mean())

# hypothesis testing using ttest_ind
print(stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade']))
print(stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade']))
print(stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade']))
print(stats.ttest_ind(early['assignment4_grade'], late['assignment4_grade']))
print(stats.ttest_ind(early['assignment5_grade'], late['assignment5_grade']))
