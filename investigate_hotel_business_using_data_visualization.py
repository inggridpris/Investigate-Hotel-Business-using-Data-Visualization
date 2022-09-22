# -*- coding: utf-8 -*-
"""Investigate Hotel Business using Data Visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ne0Pblvb3pTz1nGhX-MmootjCLD5odnd
"""

from google.colab import drive
drive.mount('/content/drive')

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

print('Numpy Version:', np.__version__)
print('Pandas Version:', pd.__version__)
print('Seaborn Version:', sns.__version__)

from matplotlib import rcParams
rcParams['figure.figsize'] = 12, 4
rcParams['lines.linewidth'] = 3
rcParams['xtick.labelsize'] = 'x-large'
rcParams['ytick.labelsize'] = 'x-large'

df= pd.read_csv('/content/drive/My Drive/Investigate Hotel Business using Data Visualization/hotel_bookings_data.csv')

df = pd.read_csv('hotel_bookings_data.csv')

df.info()

df.head()

print('Data duplicate pada dataset ini ada',df.duplicated().sum())

df1=df.drop_duplicates()

df1.duplicated().sum()

df1.isna().sum()

df1['children']=df1['children'].fillna(0)
df1['city']=df1['city'].fillna('unknown')
df1['agent']=df1['agent'].fillna(0)
df1['company']=df1['company'].fillna(0)

df1.duplicated().sum()

df1.info()

df1['children']=df1['children'].astype('int64')
df1['agent']=df1['agent'].astype('int64')
df1['company']=df1['company'].astype('int64')

df1.info()

df1['meal'].unique()

df1['meal']=df1['meal'].replace(['Undefined'],'No Meal')

df1['meal'].value_counts()

df1['total_guest']=df1['adults']+df1['children']+df1['babies']

df1['no_night']=df1['stays_in_weekend_nights']+df1['stays_in_weekdays_nights']

df1.info()

df3 = df1[(df1['total_guest'] > 0) & (df1['no_night'] > 0)]

df3.info()

df3.to_csv('hotel_bookings_datanew.csv', index=False)



df3_jp=df3.groupby(['arrival_date_month','hotel'])['arrival_date_year'].agg(['nunique','count']).reset_index()
df3_jp.columns=['month','hotel_name','yearunique','total_book']
df3_jp

"""Pada bulan oktober dan september, data yang diambil 3 tahun yang lalu sedangkan sisanya diambil 2 bulan yang lalu. maka dari itu, data ini perlu untuk di normalisasikan lagi."""

df3_jp['average_book']=round(df3_jp['total_book']/df3_jp['yearunique'])
df3_jp

order_months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
df3_jp['months']=df3_jp['month'].str[:3]
df3_jp['months']= pd.Categorical(df3_jp['months'],categories=order_months,ordered=True) 
df3_jp

plt.figure(figsize=(15,10))
sns.lineplot(x='months', y='average_book', hue='hotel_name',size='hotel_name', sizes=(5,5), data= df3_jp, palette=['purple','green'])

plt.xlabel('Arrival Month', fontsize=16)
plt.ylabel('Average Number of Booking', fontsize=16)

plt.title('Average number of Booking in City Hotel and Resort Hotel', fontsize=25)

plt.axvline(4, linestyle='-', color='blue')
plt.axvline(6, linestyle='-', color='blue')
plt.stackplot(np.arange(4,7,1),[[5000]], color='lightblue', alpha=0.5)
plt.text(x=4.7, y=4400, s='Holiday\nSeason', fontsize=16, color='red')

plt.axvline(9, linestyle='-', color='blue')
plt.axvline(11, linestyle='-', color='blue')
plt.stackplot(np.arange(9,12,1),[[5000]], color='lightblue', alpha=0.5)
plt.text(x=9.7, y=4400, s='Holiday\nSeason', fontsize=16, color='red')

plt.tight_layout()

plt.savefig('average number.jpeg',dpi=200)



df4=df3.copy()

df4.info()

df4['no_night'].unique()

df4['no_night'].value_counts()

df4['total_duration']=np.where(df4['no_night']>21,21,
                               np.where(df4['no_night']>14,15, df3['no_night']))

df4.info()

df4['total_duration'].value_counts()

df4_ph=df4.groupby(['hotel','total_duration','is_canceled']).agg({'arrival_date_month':'count'}).reset_index()

df4_ph

df4_pivot=pd.pivot_table(df4_ph, values='arrival_date_month',index=['hotel','total_duration'], columns='is_canceled').reset_index()
df4_pivot.columns=['hotel_name','total_nights','not_canceld','cancelled']
df4_pivot

df4_pivot['percent_canceled'] = round(df4_pivot['cancelled']*100.0/(df4_pivot['not_canceld']+df4_pivot['cancelled']),2)

df4_pivot

plt.figure(figsize=(15,10))
sns.barplot(x='total_nights', y='percent_canceled', hue='hotel_name',data= df4_pivot, palette=['brown','chocolate'])
sns.regplot(x='total_nights', y='percent_canceled', data=df4_pivot[df4_pivot['hotel_name'] == 'Resort Hotel'], scatter=False, label='Trend Resort Hotel', color='Khaki', truncate=False)
sns.regplot(x='total_nights', y='percent_canceled', data=df4_pivot[df4_pivot['hotel_name'] == 'City Hotel'], scatter=False, label='Trend City Hotel', color='coral', truncate=False)

plt.legend(title='Hotel Type :', title_fontsize=15, prop={'size':13})
plt.xlabel('Stay Duration', fontsize=16)
plt.ylabel('Percent of Canceled', fontsize=16)

plt.title('Percentage of canceled with duration in City Hotel and Resort Hotel', fontsize=25)

plt.tight_layout()

plt.savefig('percent canceled.jpeg',dpi=200)

df5=df4.copy()



df5.info()

df5['lead_time'].unique()

df5['lead_time'].value_counts()

df5['lead_time'].max()

df5['lead_time'].min()

df5['lead_time'].describe()

df5['total_lead_time']=np.where(df5['lead_time']>400,401,df4['lead_time'])
df5['total_lead_time'].value_counts()

df5['total_lead_time'].describe()

lt=list(np.arange(0,max(df5['total_lead_time'])+30,30))
print(lt)

lt_labels=["{0}-{1}".format(str(lt[x]), str(lt[x+1])) for x in range(len(lt[:-1]))]
print(lt_labels)

df5['lead_timenew']=pd.cut(x=df5['total_lead_time'], bins=lt, labels=lt_labels, include_lowest=True, ordered=True)
df5['lead_timenew']

df5

df5_jpjw=df5.groupby(['hotel','lead_timenew','is_canceled']).agg({'lead_time':'count'}).reset_index()
df5_jpjw

df5_pivot=pd.pivot_table(df5_jpjw, values='lead_time',index=['hotel','lead_timenew'], columns='is_canceled').reset_index()
df5_pivot.columns=['hotel_name','lead_timenew','not_canceled','canceled']
df5_pivot

df5_pivot['prg_canceled'] = round(df5_pivot['canceled']*100.0/(df5_pivot['not_canceled']+df5_pivot['canceled']),2)
df5_pivot

plt.figure(figsize=(15,10))
sns.barplot(x='lead_timenew', y='prg_canceled', hue='hotel_name',data= df5_pivot, palette=['lime','green'])

plt.axvline(0.5, linestyle='-.', color='brown')
plt.text(x=-0.5, y=65, s='1 month', fontsize=16, color='black')

plt.axvline(10.5, linestyle='-.', color='brown')
plt.axvline(12.5, linestyle='-.', color='brown')
plt.text(x=10.8, y=65, s='11-12 months', fontsize=16, color='black')

plt.legend(title='Hotel Type :', title_fontsize=15, prop={'size':13})
plt.xlabel('Lead Time Duration', fontsize=16)
plt.ylabel('Percent of Canceled', fontsize=16)

plt.title('Percentage of canceled with Lead Time duration in City Hotel and Resort Hotel', fontsize=25)

plt.tight_layout()

plt.savefig('lead time.jpeg',dpi=200)

