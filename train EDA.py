#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


train_df = pd.read_csv('train.csv')
train_df.head()
#store_nbr: 제품이 판매되는 상점
#family: 판매되는 제품의 유형
#sales: 총 매출(분수값 가능)
#onpromotion : 특정 날짜에 매장에서 프로모션중인 제품군의 총 항목 수를 나타낸다


# In[3]:


holidays_events = pd.read_csv('holidays_events.csv')
stores = pd.read_csv('stores.csv')
transactions = pd.read_csv('transactions.csv')


# In[4]:


holidays_events.head()


# In[5]:


stores.head()


# In[6]:


oil.head()


# In[ ]:


transactions.head()


# In[7]:


train_df.shape 
#train_df, transactions, stores는 store_nbr로 결합해야한다
#stores와 holiday는 location으로 결합 


# In[8]:


train_df.info()


# In[9]:


#결측값 있는지 확인, 없음
train_df.isnull().sum()


# In[10]:


print(train_df['store_nbr'].unique())
print()
print(train_df['store_nbr'].value_counts())


# In[11]:


print(train_df['family'].unique())
print()
print(train_df['family'].value_counts())


# In[12]:


print(train_df['date'].unique())
print()
print(train_df['date'].value_counts()) 


# In[13]:


print(train_df['onpromotion'].unique())
print()
print(train_df['onpromotion'].value_counts()) 


# In[14]:


import matplotlib.pyplot as plt


# In[15]:


plt.scatter(train_df['store_nbr'],train_df['sales'])


# In[16]:


plt.scatter(train_df['family'],train_df['sales'])


# In[17]:


plt.scatter(train_df['onpromotion'],train_df['sales'])


# In[18]:


plt.scatter(train_df['date'],train_df['sales'])


# In[19]:


import numpy as np # linear algebra
import pandas as pd #data processing, CSV file I/O (e.g. pd.read_csv)
import math

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots


# In[20]:


get_ipython().system('pip install plotly')


# In[21]:


#https://www.kaggle.com/javi23ruiz/eda-with-plotly-useful-conclusions
train_aux = train_df[['date', 'sales', 'onpromotion']].groupby('date').mean()
train_aux = train_aux.reset_index()
fig = go.Figure(data=go.Scatter(x=train_aux['date'], 
                                y=train_aux['sales'],
                                marker_color='red', text="sales"))
fig.update_layout({"title": f'Avg Sales by date for all stores and products',
                   "xaxis": {"title":"Date"},
                   "yaxis": {"title":"Avg Unit Sold"},
                   "showlegend": False})
fig.show()


# In[10]:


# oil_df


# In[23]:


oil = pd.read_csv('oil.csv')
oil.head()


# In[24]:


#https://www.kaggle.com/javi23ruiz/eda-with-plotly-useful-conclusions
rain_aux = train_df[['date', 'sales']].groupby('date').mean()
train_aux = train_aux.reset_index()
fig = go.Figure(data=go.Scatter(x=oil['date'], 
                                y=oil['dcoilwtico'],
                                marker_color='blue', text="sales"))


fig.update_layout({"title": f'Oil Prices Chart',
                   "xaxis": {"title":"Date"},
                   "yaxis": {"title":"Oil Price"},
                   "showlegend": False})
fig.show()

#유가가 낮아지면 소비자의 구매력이 높아진다


# In[22]:


#holidays_events


# In[37]:


#https://www.kaggle.com/ilyakondrusevich/54-stores-54-models
def strip_spaces(a_str_with_spaces):
    return a_str_with_spaces.replace(' ', '')

holidays = pd.read_csv('holidays_events.csv', index_col='date',
                       parse_dates=['date'], infer_datetime_format=True,
                       converters={'locale_name': strip_spaces})  # removes spaces from locale_name

holidays.head()


# In[45]:


holidays.shape


# In[25]:


print(holidays_events['type'].unique())
print()
print(holidays_events['type'].value_counts())


# In[30]:


holidays_events['locale'].value_counts()


# In[31]:


holidays_events['locale_name'].value_counts()


# In[39]:


holidays.isna().sum()


# In[43]:


#캘린더에 workday인지 아닌지 채워야한다
# Calendar
holidays_rdy = pd.DataFrame(index=pd.date_range('2013-01-01', '2017-08-31'))
holidays_rdy['day_of_week'] = holidays_rdy.index.dayofweek + 1  # Monday = 1, Sunday = 7
holidays_rdy['work_day'] = True 
holidays_rdy.loc[holidays_rdy['day_of_week'] > 5, 'work_day'] = False  # False for saturdays 
holidays_rdy[0:30]


# In[44]:


duplicates = holidays[holidays.index.duplicated(keep=False)]
print(duplicates['locale_name'])


# In[ ]:




