#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[155]:


k=train_df.groupby('date')
k


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


# # 1/29일

# 홀리데이 변수 만들기

# In[71]:


holidays = pd.read_csv('holidays_events.csv')
holidays.set_index('date', inplace=True)
holidays


# In[72]:


print('Holidays types:', holidays['type'].unique())
print('Holidays region types:', holidays['locale'].unique()) 
print('Holidays locale names:', holidays['locale_name'].unique()) 


# In[152]:


holidays_rdy = pd.DataFrame(index=pd.date_range('2013-01-01', '2017-08-31')) #1704rows
holidays_rdy['day_of_week'] = holidays_rdy.index.dayofweek + 1  # Monday = 1, Sunday = 7 , 우리나라기준 2013,01,01 (화요일)
holidays_rdy['work_day'] = True
holidays_rdy.loc[holidays_rdy['day_of_week'] > 5, 'work_day'] = False  # False for saturdays and sundays 
holidays_rdy


# In[74]:


# 홀리데이데이터 셋의 중복값 제거  (holidays의 날짜에 중복값이 있는지에 대해 확인)
duplicates = holidays[holidays.index.duplicated(keep=False)] #duplicated : 중복값 확인해주는 함수, keep=False: 중복이면 True
print(duplicates['locale_name'])


# In[153]:


duplicates = [('2012-06-25', 'Latacunga Machala'), ('2012-07-03', 'ElCarmen'),
              ('2012-12-22', 'Ecuador'), ('2012-12-24', 'Ecuador'),
              ('2012-12-31', 'Ecuador'), ('2013-05-12', 'Ecuador'),
              ('2013-06-25', 'Machala Latacunga'), ('2013-07-03', 'SantoDomingo'),
              ('2013-12-22', 'Salinas'), ('2014-06-25', 'Machala Imbabura Ecuador'),
              ('2014-07-03', 'SantoDomingo'), ('2014-12-22', 'Ecuador'),
              ('2014-12-26', 'Ecuador'), ('2015-06-25', 'Imbabura Latacunga'),
              ('2015-07-03', 'SantoDomingo'), ('2015-12-22', 'Salinas'),
              ('2016-04-21', 'Ecuador'), ('2016-05-01', 'Ecuador'),
              ('2016-05-07', 'Ecuador'), ('2016-05-08', 'Ecuador'),
              ('2016-05-12', 'Ecuador'), ('2016-06-25', 'Imbabura Latacunga'),
              ('2016-07-03', 'SantoDomingo'), ('2016-07-24', 'Guayaquil'),
              ('2016-11-12', 'Ecuador'), ('2016-12-22', 'Salinas'),
              ('2017-04-14', 'Ecuador'), ('2017-06-25', 'Latacunga Machala'),
              ('2017-07-03', 'SantoDomingo'), ('2017-12-08', 'Quito'),
              ('2017-12-22', 'Ecuador')]

holidays = holidays.groupby(holidays.index).first() # we left only first, but we need others too
for date, locale_name in duplicates:
    holidays.loc[date, 'locale_name'] = holidays.loc[date, 'locale_name'] + ' ' + locale_name
    
holidays[1:20]


# In[76]:


# Apply holidays to calendar
holidays_rdy = holidays_rdy.merge(holidays, how='left', left_index=True, right_index=True)
holidays_rdy


# In[24]:


# type column: 'Work Day'
holidays_rdy.loc[holidays_rdy['type'] == 'Work Day', 'work_day'] = True

# type column: 'Holiday', 'Transfer', 'Additional', 'Bridge'
holidays_rdy.loc[(holidays_rdy['type'] == 'Holiday') &
                 (holidays_rdy['locale_name'].str.contains('Ecuador', na=False)),
                 'work_day'] = False
holidays_rdy.loc[(holidays_rdy['type'] == 'Transfer') & 
                 (holidays_rdy['locale_name'].str.contains('Ecuador', na=False)),  
                 'work_day'] = False
holidays_rdy.loc[(holidays_rdy['type'] == 'Additional') & 
                 (holidays_rdy['locale_name'].str.contains('Ecuador', na=False)),
                 'work_day'] = False
holidays_rdy.loc[(holidays_rdy['type'] == 'Bridge') & 
                 (holidays_rdy['locale_name'].str.contains('Ecuador', na=False)),   
                 'work_day'] = False
holidays_rdy

holidays_rdy.drop(columns = ['locale'], axis=1, inplace=True)

# transferred column
holidays_rdy.loc[holidays_rdy['transferred'] == True, 'work_day'] = True


# In[ ]:


events = holidays_rdy[holidays_rdy['type']=='Event']
events

holidays_rdy.loc[holidays_rdy['description'].str.contains('Terremoto', na=False),
                 'description'] = 'Earthquake'
holidays_rdy.loc[holidays_rdy['description'].str.contains('futbol', na=False), 
                 'description'] = 'Football'
events = holidays_rdy[holidays_rdy['type']=='Event']

# Check for misspells
print(events['description'].unique())
#['Dia de la Madre' 'Football' 'Black Friday' 'Cyber Monday' 'Earthquake']


# Print mean sales 
sales = train_df.groupby(['date']).sales.sum()
events = events.merge(sales, how='left', left_index=True, right_index=True)
print(events.groupby(['description']).sales.mean())
print('All sales mean:', sales.mean())


# Imprecise method because we do not have enough data, but Earthquake and Cyber Monday definitely should be considered during training, + Black Friday.
# Sales are not depends much on Football and Mother's day.

# # oil nan값 처리

# In[88]:


oil = pd.read_csv('oil.csv')
oil['date'] = pd.to_datetime(oil['date'])
oil


# In[89]:


oil = oil.set_index('date')['dcoilwtico'].resample(
    'D').sum().reset_index()  # #시간간격 재조정 + 결측값 0으로 채우기
oil


# In[92]:


oil['dcoilwtico'] = np.where(oil['dcoilwtico']==0, np.nan, oil['dcoilwtico']) 
oil[0:7]


# In[93]:


oil['dcoilwtico_interpolated'] = oil.dcoilwtico.interpolate()  # 결측값보간 

oil.head(10)


# In[101]:


oil_rdy = oil.loc[:, ['date', 'dcoilwtico_interpolated']]
oil_rdy.iloc[0, 1] = 93.1


# In[102]:


oil_rdy.isna().sum().sum
oil_rdy['date'] = pd.to_datetime(oil_rdy['date'])
oil_rdy


# In[103]:


oil_rdy['date'] = oil_rdy['date'].dt.to_period('D')
oil_rdy = oil_rdy.set_index(['date'])
oil_rdy


# # onpromotion

# In[116]:


train_df['onpromotion'].value_counts()


# In[115]:


pro0 = train_df['onpromotion'] == 0
pro0_df = train_df.loc[pro0,:]
pro0_df['sales'].mean()


# In[107]:


onpromotion_sales_means = train_df.groupby('onpromotion').agg({'sales' : 'mean'}).reset_index().sort_values(by='sales', ascending=False)
onpromotion_sales_medians = train_df.groupby('onpromotion').agg({'sales' : np.median}).reset_index().sort_values(by='sales', ascending=False)


# In[109]:


onpromotion_sales_means


# In[108]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.figure(figsize = (20,5))
sns.lineplot(x = onpromotion_sales_means.onpromotion, y = onpromotion_sales_means.sales, color = 'r', label = 'Means', alpha = 0.3)
sns.lineplot(x = onpromotion_sales_medians.onpromotion, y = onpromotion_sales_medians.sales, color = 'g', label = 'Middle', alpha = 0.3)
plt.legend()
plt.title('Hoilday_type : Comparsion with Mean and Middle')


# In[ ]:


_ = plot_pacf(calendar.avg_oil, lags = 12) # 자기상관플롯, (자기상관은 시계열 분석에서 사용하는 상관계수)


# # oil

# In[117]:


#https://www.kaggle.com/ekrembayar/store-sales-ts-forecasting-a-comprehensive-guide


# In[126]:


train_df.head()


# In[136]:


highoil = train_df['date'] <= '2014-11-31'
highoil_df = train_df.loc[highoil,:]
lowoil = train_df['date'] > '2014-11-31'
lowoil_df = train_df.loc[lowoil,:]


# In[150]:


high_df = highoil_df.groupby('family').agg({'sales' : 'mean'}).reset_index().sort_values(by='sales', ascending=False)
low_df = lowoil_df.groupby('family').agg({'sales' : 'mean'}).reset_index().sort_values(by='sales', ascending=False)
low_df


# In[151]:


high_df
#GROCERY 1 , BEVERAGES, PRODUCE(1400정도)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




