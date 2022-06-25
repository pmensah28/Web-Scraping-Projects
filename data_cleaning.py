# _*_ coding: utf-8 _*_
"""
Created on Fri June 24 15:13:05 2022

@author:Prince
"""
import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')
# print(df.columns)
# print(df.shape)

#Getting started with Salary Parsing
df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Employer_Provided_Salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)
# print(df.hourly)
# print(df.Employer_Provided_Salary)
df = df[df['Salary Estimate'] !='-1'] #Remove '-1' from Salary Estimates
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0]) #Write a function to split the inscriptions in Salary Estimate column.
# print(salary)
remove_Kd = salary.apply(lambda x: x.replace('K','').replace('$','')) #Write a function to remove 'K' and '$' in Salary Estimate
# print(remove_Kd)
min_hr = remove_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))
# print(remove_hr)
df['Min_Salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['Max_Salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
# print(df.Min_Salary)
# print(df.Max_Salary)
df['Avg_Salary'] = (df.Min_Salary+df.Max_Salary)/2

#Now let's Company Name txt only.
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)
#df job state
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
# print(df.job_state.value_counts())
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)
#age
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2022-x)
#Job Description
# print(df['Job Description'][56])
#Parsing of job description
#job
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['tableau_yn'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
# print(df.tableau_yn.value_counts())
# print(df.columns)
df_drop = df.drop(['Unnamed: 0'], axis=1)
df_drop.to_csv('cleaned_salary_data.csv', index=False)
data = pd.read_csv('cleaned_salary_data.csv')
# print(data.head(10))