import pandas as pd

# function for returning the sum of the Employees of all Department where the Country is India

def sum_of_emp():
  object_2=['India']
  r_df2 = df2.loc[df2['COUNTRY'].isin(object_2)]
  object_1=r_df2['CODE'].tolist()
  r_df1 = df1.loc[df1['COMPANY_CODE'].isin(object_1)]
  allemp=r_df1['TOTAL_EMPLOYEES'].tolist()

  return allemp

Department={'ID':[1,2,3,4,5,],
'NAME':['Engineering & Technology','Sales, Service & Support','Marketing & Communications','Business Strategy','Marketing & Communications'],
'COMPANY_CODE':['A101','B102','C103','D104','E105'],
'TOTAL_EMPLOYEES':[100,110,120,130,140]}

Company={'CODE':['A101','B102','C103','D104','E105'],
'NAME':['GOOGLE','MICROSOFT','GOOGLE','MICROSOFT','KPMG'],
'COUNTRY':['India','Australia','India','Australia','Netherlands'],
'TOTAL_EMPLOYEES':[500,1000,250,600,100]}

df1=pd.DataFrame(Department)
df2=pd.DataFrame(Company)

soe=sum_of_emp()
for i in range(0,len(soe)):
  soe[i]=int(soe[i])
sum_of_the_employees=sum(soe)
print('The sum of the employees of all department where the country (India) is {}'.format(sum_of_the_employees))
