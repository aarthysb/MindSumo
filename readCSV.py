__author__ = 'Aarthy'
import pandas as pd
from pandas import DataFrame
import datetime

df = pd.read_csv('subscription_report.csv', index_col= 'Id', parse_dates = True)
df.columns = ['SubId', 'Amount', 'Date']

subIds = df['SubId'].unique()

for id in subIds:
    newdf = df[df['SubId'] == id]
    newdf.sort_values(by='Date')
    dates = newdf['Date'][:2]
    dates = dates.values
    if(len(dates)>1):
        date1 = datetime.datetime.strptime(dates[1], '%m/%d/%Y')
        date2 = datetime.datetime.strptime(dates[0], '%m/%d/%Y')
        diff = date1 - date2
        if diff.days == 1:
            print id, 'Daily'
        elif diff.days <= 31:
            print id, 'Monthly'
        else:
            print id, 'Yearly'
    else:
        print id, 'one-off'

#print df.head()