import pandas as pd


# First we create two DataFrames, staff and students. There's some overlap in these DataFrames, in that James and Sally
# are both students and staff, but Mike and Kelly are not. Importantly, both DataFrames are indexed along the value we
# want to merge them on, which is called Name.
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())

# If we want the union of these, we would call merge passing in the DataFrame on the left and the DataFrame on the right
# , and telling merge that we want it to use an outer join. We tell merge that we want to use the left and right indices
# as the joining columns.
print(pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True))
#  If we wanted to get the intersection, that is, just those students who are also staff, we could set the how attribute
#  to inner. And we set the resulting DataFrame has only James and Sally in it.
print(pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True))
# all staff
print(pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True))
# all student
print(pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True))

# using columns to join instead of indices
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
print(pd.merge(staff_df, student_df, how='left', right_on='Name', left_on='Name'))

# conflicting data columns - i.e., same column name in both dfs
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
# added Location column to both dfs
print(pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name'))
# The merge function preserves this information, but appends an _x or _y to help differentiate between which index went
# with which column of data. The _x is always the left DataFrame information, and the _ y is always the right DataFrame

# merging using multiple columns
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
print(staff_df)
print(student_df)
print(pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name']))
