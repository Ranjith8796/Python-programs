import pandas as pd

def change_datetime(i):
    year=i[-4:]
    month='-09-'
    date=i[:2]
    convertedformat=year+month+date 
    return convertedformat

'''input'''
Dates= {'dates': ['05Sep2009','13Sep2011','21Sep2010']}

df=pd.DataFrame(Dates)
oldlist=df['dates'].tolist()

newlist=[]
for i in oldlist:   
    newlist.append(change_datetime(i))
Dates['dates']=newlist

'''output'''
print(Dates)




