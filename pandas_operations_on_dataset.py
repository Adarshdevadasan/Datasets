# -*- coding: utf-8 -*-
"""Pandas operations on dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/169eIfeMDGZxYL621dvTV5g1htP2jZVFi
"""

import pandas as pd
import numpy as np

s=pd.read_csv("/content/drive/MyDrive/database.csv")

s

s.head()

s.tail()

s.describe()

s.transpose()

s.to_numpy

s.sort_index

s.sort_values

s.iloc[3]

s.iloc[3:5]

s.iloc[3:6,0:5]

s.isnull()

s.fillna(s.median())

s.isnull().sum()

s.dropna()

s.isnull().sum()

s.mean()

s.value_counts

s.stack()

s.unstack()

s.dtypes

s['new']=s['Landing Type']+s['Landing Outcome']
s

s.drop('new',axis=1)

s.loc[40]

s.loc[40,'Landing Type']

s.iloc[30:42],['Payload Name','Payload type']

s.reset_index

space='AD','AS','TY','OP','KM','JB','RT','QW','QA','AZ','AD','AS','TY','OP','KM','JB','RT','QW','QA','AZ','AD','AS','TY','OP','KM','JB','kk','RT','QW','QA','AZ','AD','AS','TY','OP','KM','JB','RT','QW','QA','AZ'.split()
s['states']=space
s

s.set_index("states",inplace=True)
s

s.index.names

s.xs('AZ')

s.xs("RT")

s.groupby("Flight Number")

by_fly=s.groupby("Flight Number")

by_fly

by_fly.mean()

by_fly.std()

by_fly.min()

by_fly.max()

by_fly.count()

by_fly.describe().transpose()
