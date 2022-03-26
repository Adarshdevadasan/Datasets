# -*- coding: utf-8 -*-
"""pandas2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DxvH1_wudH0rDSh15bU1D0TXUpixxQEo
"""

import pandas as pd
import numpy as np

# to create series 
# np.nan is a null value 

s=pd.Series([1,2,3,4,5,6,np.nan,8,9,10])

# to create a dataframe by passing a numpy array with datatime index and label columns
d=pd.date_range('20210928',periods=10)
d

# to create a dataframe
#the np.random.randn() function creates an array of specified shape and fills it with values as per standard normal distribution.
# column name with labels A,B,C,D
#index of the dataframe is the d and it contains datatime index

df=pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])
df

# create a dataframe by dictionary of objects and it converted into a series

df1=pd.DataFrame({'A':[1,2,3,4],
                  'B':pd.Timestamp('20210928'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':np.array([5]*4,dtype='int32'),
                  'E':pd.Categorical(['true','false','true','false']),
                  'F':'pandas'})
df1

# to check the data type

df1.dtypes

df.dtypes

# vies the data 
# it will give the first 5 values

df.head()

# to get the last 5 values
df.tail()

# to get the index of the dataframe
df.index

# to get the column of the dataframe
df.columns

# to get the numpy representation of the data
df.to_numpy()

# to describe the data
df.describe()

# dataframe sorted by index
df.sort_index(axis=1,ascending=False)

# sorting the dataframe by values
# it sort the dataframe depending on 'c'
df.sort_values(by='C')

# to access only the single column
df['C']

# to slice the rows
# it will give the result from 0th row to 3rd row

df[0:3]

# to select the data by using labels
# inside the method, we can pass the values by labels

df.loc[d[0]]

# to selecting data on a multi axis by label
df.loc[:,['A','C']]

# to get the date with same range
df.loc['20210928':'20211003',['D','C']]

# to get a single element from the dataframe
df.loc['20210928',['D','C']]

# to get a single element from the dataframe
df.loc[d[0],['D','C']]

# to get the exact value  in 0th index at column 'c'
df.at[d[0],'C']

# selecting a value from using the position inside the dataframe
# it will select all the value from the third position
df.iloc[3]

# to select the value in the 3rd and 4th position
df.iloc[3:5]

# to select the value in 3rd and 4th row,and it only include the column strat with 0 and end with 2.
df.iloc[3:5,0:2]

# boolean indexing
# it will show the value in 'A' which is greater than 'B'
df[df['A']>0]

df[df['A']>2]

df[df['A']>3]

# handling the missing values
df2=df.reindex(index=d[0:4],columns=list(df.columns)+['E'])
df2.loc[d[0]:d[1],'E']=1
df2

# to check the null values
df2.isnull()

# to drop the column
# it will drop the null values presented in the dataframe
df2.dropna()

# fill the missing data
# it will fill the missing values with 2
df2.fillna(value=2)

# describe statistics 
# to find the mean
df.mean()

s=pd.Series([1,2,3,np.nan,4,5,6,7,8,9],index=d).shift(2)
s

# it subtract all elements of df by s
df.sub(s,axis='index')

df

# to apply some functions
# cumsum is used to find the cumlative sum value over any axis.
df.apply(np.cumsum)

# lambda function will take any number of arguments but can have only one expression
# it give the subtraction if x.max and x.min
df.apply(lambda x:x.max()-x.min())

# histograms---histogram is a representation of distribution of dat a
#  the value_counts() function returns a series that contain counts of uniwue values.
s.value_counts()

s=pd.Series(['pandas','python','jupiter',np.nan,'java','colab'])
 # string method inside pandas
s.str.upper()

df=pd.DataFrame(np.random.randn(10,4))
df

# break the dataframe
df2=[df[:3],df[3:7],df[7:]]
df2

# concat the serveral pieces
pd.concat(df2)

# left joining
left=pd.DataFrame({'A':[1,2],'B':[3,4]})

# right joining
right=pd.DataFrame({'A':[3,2],'D':[4,5]})

left

right

pd.merge(left,right,on='A')

df

# Grouping
df.groupby([2,3]).sum()

# reshape the dataframe
my_tuple=list(zip(*[[1,2,3,4,5,17,18,19],[11,12,13,6,7,8,9,10]]))
index=pd.MultiIndex.from_tuples(my_tuple,names=['first','second'])
df=pd.DataFrame(np.random.randn(8,2),index=index,columns=['A','B'])
df2=df[:2]
df2

df2.stack()

# stack has a multiindex as indexes
# inverse stack is unstack
df2.unstack()

# private table
df=pd.DataFrame({'A':['a','c','c','d']*3,
              'B':['A','B','C']*4,
              'C':['P','P','P','Q','Q','Q']*2,
              'D':np.random.randn(12),
              'E':np.random.randn(12)})
df

#pd.pivot_table(df,values='D',index=['A','B'],columns=['C'])

dates =pd.date_range('30/09/2021 00:00',periods=5,freq='s')
dates

ts=pd.Series(np.random.randint(len(dates)),dates)

ts

ts_utc=ts.tz_localize('UTC')

ts_utc

ts_utc.tz_convert('US/Eastern')

dates=pd.date_range('30/09/2021',periods=5,freq='M')
dates

ts=pd.Series(np.random.randint(len(dates)),dates)
ts

ps=ts.to_period()

ps

ps.to_timestamp()

df=pd.DataFrame({'id':[1,2,3,4,5,6],
                "grade":['a','b','c','b','a','e']})

df

df['grade']=df['grade'].astype("category")
df["grade"]

df["grade"].cat.categories=["good",'very bad','very good','exellent']

df["grade"]=df['grade'].cat.set_categories(['very good','bad','very bad','good','medium'])
df["grade"]





