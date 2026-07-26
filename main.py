#students result analysis project

import pandas as pd
import numpy as np

df = pd.read_csv('results.csv')

# print(df.tail(5))
# print(df.shape)
# print(df.columns)
# print(df.isna().sum())
# print(df.describe())
df.drop(columns=['Unnamed: 0','Div'],inplace=True)
print(df.columns)

#student data set 
#student who got the highest marks in the exam
highest_marks = df[df['Total'] == df['Total'].max()]
print("student who got the highest marks in the exam ")
print(highest_marks)


#lowest marks in the exam 
lowest_marks = df[df['Total'] == df['Total'].min()]
print("student who got the lowest marks in theexam ")
print(lowest_marks)


#highest marks in each subject
highest_marks_each_subject =df[['Hindi', 
'English', 
'Science',
 'Maths', 
'History', 
'Geograpgy']].max()
print("highest marks in each subject")
print(highest_marks_each_subject)

#highest marks in each subject with student name
highest_marks_each_subject_with_student_name = df.loc[df[['Hindi',
 'English',
 'Science', 
'Maths',
 'History',
 'Geograpgy']].idxmax()]
print("highest marks in each subject with student name")
print(highest_marks_each_subject_with_student_name)


#lowest marks in each subject
lowest_marks_each_subject = df[['Hindi', 
'English', 
'Science', 
'Maths', 
'History', 
'Geograpgy']].min()
print("Lowest  makrs in each subject ")
print(lowest_marks_each_subject)


#lowest marks in each subject with student name
lowest_marks_each_subject_with_student_name = df.loc[df[['Hindi', 
'English', 
'Science',
 'Maths', 
'History', 
'Geograpgy']].idxmin()]
print("lowest marks in each subject with student name")
print(lowest_marks_each_subject_with_student_name)

#students who passed in each subject
passed_students_each_subject = df[(df[['Hindi', 
'English', 
'Science',
 'Maths', 
'History', 
'Geograpgy'] ]>=33).all(axis=1)  & (df['Total'] >= 198)]
print("students who passed in each subject")
print(passed_students_each_subject)


#students who failed in exam
failed_students = df[(df['Total']<198) | (df[['Hindi', 
'English', 
'Science', 
'Maths', 
'History', 
'Geograpgy']] < 33).any(axis=1)]
print("students who failed in exam ")
print(failed_students)


#student who failed in each subject
students_failed_in_each_subject = df.loc[(df[['Hindi',
 'English', 
'Science', 
'Maths', 
'History', 
'Geograpgy']] < 33).any(axis=1) & (df['Total']< 198)]
print("students who failed in each subject")
print(students_failed_in_each_subject)

#students percentage 
df["Percentage"] = (df['Total']/600)*100
df.sort_values(by='Percentage', ascending=False, inplace=True)
print(df['Percentage'])

#students who got distinction 
distinction_students = df[df['Percentage'] >= 75]
print("students who got the distinction")
print(distinction_students)

#Subject wise statistics
subjects = ['Hindi',
 'English', 
'Science', 
'Maths',
 'History',
 'Geograpgy']

print("subject wise statistics ")

for subject in subjects:
    print(f"statistics for {subject}: \n")
    print(f'highest marks in {subject} : {df[subject].max()}')
    print(f'lowest marks in {subject} : {df[subject].min()}')
    print(f'average marks in {subject} : {df[subject].mean()}' )
    
    #passed percentage 
overall_passed_percentage = (len(passed_students_each_subject)/len(df))*100
print(f"passed percentage : {overall_passed_percentage:.2f}%")

 #failed percentage 
overall_failed_percentage = (len(failed_students)/len(df))*100
print(f"failed percentage : {overall_failed_percentage:.2f}%")


#top 10 students based on percentage
top_10 = df.nlargest(10,"Percentage")
print("top 10 students :\n")
print(top_10)

#bottom 10 students based on percentage 

bottom_10 = df.nsmallest(10,"Percentage")
print("bottom 10 students :\n")
print(bottom_10)


#students scoring above 80 percentage
above80 =  df[df['Percentage'] > 80]
print("students scoring above 80 percentage :\n")
print(above80)

#students scoring below 40 percentage
below40 = df[df['Percentage'] < 40]
print("students scoring below 40 percentage :\n")
print(below40)

df.to_csv("results_analysis.csv",index=False)

#terminal printss 
# Index(['Hindi', 'English', 'Science', 'Maths', 'History', 'Geograpgy', 'Total',
#        'Results'],
#       dtype='str')
# student who got the highest marks in the exam 
#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results
# 532     88       91       97     93       94         42    505        1
# student who got the lowest marks in theexam 
#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results
# 45      33       13       30      2        3         22    103        0
# 217      8       25       24     18       28          0    103        0
# highest marks in each subject
# Hindi        99
# English      99
# Science      99
# Maths        99
# History      99
# Geograpgy    99
# dtype: int64
# highest marks in each subject with student name
#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results
# 245     99       68       50     89       97         47    450        1
# 251     77       99       78     57       73         53    437        1
# 102     96       13       99     46       23         84    361        0
# 2        7       85       76     99       60         25    352        0
# 195     86       76       32     25       99         72    390        0
# 234     73       11       62     59       80         99    384        1
# Lowest  makrs in each subject 
# Hindi        0
# English      0
# Science      0
# Maths        0
# History      0
# Geograpgy    0
# dtype: int64
# lowest marks in each subject with student name
#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results
# 260      0       31       68     93       82         93    367        0
# 211     36        0       17     43       84         92    272        0
# 122     12       60        0     40        3         70    185        0
# 104      7       20       27      0       84         13    151        0
# 59      17       26        8     66        0         38    155        0
# 65      27       92       28     43       71          0    261        0
# students who passed in each subject
#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results
# 3       88       46       59     94       52         38    377        1
# 9       53       85       96     76       83         62    455        1
# 15      52       55       39     93       58         46    343        1
# 29      93       41       42     98       72         84    430        1
# 60      50       66       41     99       89         94    439        1
# ..     ...      ...      ...    ...      ...        ...    ...      ...
# 983     95       65       89     39       56         73    417        1
# 984     84       82       46     74       54         46    386        1
# 986     94       61       61     91       65         59    431        1
# 992     55       94       59     68       82         89    447        1
# 999     75       78       68     33       79         91    424        1

# [95 rows x 8 columns]
# students who failed in exam 
#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results
# 0       65       10       59      3       71         37    245        0
# 1       94       56        4     67       91         50    362        1
# 2        7       85       76     99       60         25    352        0
# 4       39       81       37     38        6         54    255        1
# 5       51       43       14     53       64         59    284        1
# ..     ...      ...      ...    ...      ...        ...    ...      ...
# 994     94       62       68     84       13         35    356        1
# 995     55       89       68     58       13         13    296        0
# 996     42       62       25     87       51         68    335        1
# 997      9       83       70     14       11         78    265        0
# 998     23       82       31     42       84         52    314        0

# [905 rows x 8 columns]
# students who failed in each subject
#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results
# 10      61       17       16     16       20         48    178        0
# 22       6       44        8     62       13         29    162        0
# 25      51       75        8      7       35          2    178        0
# 32      22       51        9     14       76         22    194        0
# 45      33       13       30      2        3         22    103        0
# ..     ...      ...      ...    ...      ...        ...    ...      ...
# 921     15       54        3     52        7         18    149        0
# 928      9        1        2     64       14         59    149        0
# 979     12       79       13     28        1          4    137        0
# 989     10        4       65      3       46         26    154        0
# 990     30       68       30     14       16          6    164        0

# [81 rows x 8 columns]
# 532    84.166667
# 834    80.166667
# 681    79.833333
# 192    79.666667
# 612    79.000000
#          ...    
# 328    20.333333
# 384    19.333333
# 586    18.166667
# 217    17.166667
# 45     17.166667
# Name: Percentage, Length: 1000, dtype: float64
# students who got the distinction
#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results  Percentage
# 532     88       91       97     93       94         42    505        1   84.166667
# 834     96       96       82     87       67         53    481        1   80.166667
# 681     74       88       90     74       69         84    479        1   79.833333
# 192     81       39       99     90       80         89    478        1   79.666667
# 612     76       93       70     85       51         99    474        1   79.000000
# 573     89       90       99     90       63         36    467        1   77.833333
# 189     65       91       29     96       84         98    463        1   77.166667
# 670     99       90       81     60       83         50    463        1   77.166667
# 878     68       73       79     81       78         83    462        1   77.000000
# 565     95       98       78     98       23         70    462        1   77.000000
# 149     87       96       61     56       74         86    460        1   76.666667
# 242     96       93       89     38       93         49    458        1   76.333333
# 9       53       85       96     76       83         62    455        1   75.833333
# 783      0       96       98     73       97         91    455        1   75.833333
# 951     89       92       97     55       26         93    452        1   75.333333
# 245     99       68       50     89       97         47    450        1   75.000000
# subject wise statistics 
# statistics for Hindi: 

# highest marks in Hindi : 99
# lowest marks in Hindi : 0
# average marks in Hindi : 51.645
# statistics for English: 

# highest marks in English : 99
# lowest marks in English : 0
# average marks in English : 50.11
# statistics for Science: 

# highest marks in Science : 99
# lowest marks in Science : 0
# average marks in Science : 49.44
# statistics for Maths: 

# highest marks in Maths : 99
# lowest marks in Maths : 0
# average marks in Maths : 49.553
# statistics for History: 

# highest marks in History : 99
# lowest marks in History : 0
# average marks in History : 49.034
# statistics for Geograpgy: 

# highest marks in Geograpgy : 99
# lowest marks in Geograpgy : 0
# average marks in Geograpgy : 50.028
# passed percentage : 9.50%
# failed percentage : 90.50%
# top 10 students :

#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results  Percentage
# 532     88       91       97     93       94         42    505        1   84.166667
# 834     96       96       82     87       67         53    481        1   80.166667
# 681     74       88       90     74       69         84    479        1   79.833333
# 192     81       39       99     90       80         89    478        1   79.666667
# 612     76       93       70     85       51         99    474        1   79.000000
# 573     89       90       99     90       63         36    467        1   77.833333
# 189     65       91       29     96       84         98    463        1   77.166667
# 670     99       90       81     60       83         50    463        1   77.166667
# 878     68       73       79     81       78         83    462        1   77.000000
# 565     95       98       78     98       23         70    462        1   77.000000
# bottom 10 students :

#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results  Percentage
# 217      8       25       24     18       28          0    103        0   17.166667
# 45      33       13       30      2        3         22    103        0   17.166667
# 586     32        1       12     22       41          1    109        0   18.166667
# 384     61       20       18      5        6          6    116        0   19.333333
# 328     65        4       33      6        3         11    122        0   20.333333
# 841      5       13       14     38       38         15    123        0   20.500000
# 816     17       23       21      4       17         45    127        0   21.166667
# 979     12       79       13     28        1          4    137        0   22.833333
# 299      7       20        1     30       75          5    138        0   23.000000
# 665     40       11       39     11       28          9    138        0   23.000000
# students scoring above 80 percentage :

#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results  Percentage
# 532     88       91       97     93       94         42    505        1   84.166667
# 834     96       96       82     87       67         53    481        1   80.166667
# students scoring below 40 percentage :

#      Hindi  English  Science  Maths  History  Geograpgy  Total  Results  Percentage
# 858     76       26        9     91       23         14    239        0   39.833333
# 654      2       73       81      5       42         36    239        0   39.833333
# 124     45       32       37     82        1         42    239        0   39.833333
# 937     83        8        0     33       74         41    239        0   39.833333
# 494     21        2       13     98       21         84    239        0   39.833333
# ..     ...      ...      ...    ...      ...        ...    ...      ...         ...
# 328     65        4       33      6        3         11    122        0   20.333333
# 384     61       20       18      5        6          6    116        0   19.333333
# 586     32        1       12     22       41          1    109        0   18.166667
# 217      8       25       24     18       28          0    103        0   17.166667
# 45      33       13       30      2        3         22    103        0   17.166667

# [194 rows x 9 columns]

