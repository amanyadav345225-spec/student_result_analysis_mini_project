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
'geography']].max()
print("highest marks in each subject")
print(highest_marks_each_subject)

#highest marks in each subject with student name
highest_marks_each_subject_with_student_name = df.loc[df[['Hindi',
 'English',
 'Science', 
'Maths',
 'History',
 'geography']].idxmax()]
print("highest marks in each subject with student name")
print(highest_marks_each_subject_with_student_name)


#lowest marks in each subject
lowest_marks_each_subject = df[['Hindi', 
'English', 
'Science', 
'Maths', 
'History', 
'geography']].min()
print("Lowest  makrs in each subject ")
print(lowest_marks_each_subject)


#lowest marks in each subject with student name
lowest_marks_each_subject_with_student_name = df.loc[df[['Hindi', 
'English', 
'Science',
 'Maths', 
'History', 
'geography']].idxmin()]
print("lowest marks in each subject with student name")
print(lowest_marks_each_subject_with_student_name)

#students who passed in each subject
passed_students_each_subject = df[(df[['Hindi', 
'English', 
'Science',
 'Maths', 
'History', 
'geography'] ]>=33).all(axis=1)  & (df['Total'] >= 198)]
print("students who passed in each subject")
print(passed_students_each_subject)


#students who failed in exam
failed_students = df[(df['Total']<198) | (df[['Hindi', 
'English', 
'Science', 
'Maths', 
'History', 
'geography']] < 33).any(axis=1)]
print("students who failed in exam ")
print(failed_students)


#student who failed in each subject
students_failed_in_each_subject = df.loc[(df[['Hindi',
 'English', 
'Science', 
'Maths', 
'History', 
'geography']] < 33).any(axis=1) & (df['Total']< 198)]
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
 'geography']

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

