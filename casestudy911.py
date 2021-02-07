import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('911.csv')

# top 5 zip codes
top_zip = data['zip'].value_counts().head(5)

# top 5 townships
top_twp = data['twp'].value_counts().head(5)

# count of unique titles
title_count = data['title'].nunique()

# taking reason from title
reason = data['title'].apply(lambda x :x.split(':')[0])

# creating a new column for reasons
data['reason'] = reason

# most common reason
common_reason = data['reason'].value_counts().head(5)

# plot for reasons
# sns.countplot(x='reason',data=data,palette='Set1',order=data['reason'].value_counts().sort_values(ascending=False).index[:50])
# sns.countplot(x=data.twp,order=data['twp'].value_counts().sort_values(ascending=False).index[:50],palette='Set1')

# plt.show()


# data cleaning
# by adding new columns as hour, day of week, time, from string type data to time
data['timeStamp'] = pd.to_datetime(data['timeStamp'])

# for hour column
data['hour'] = data['timeStamp'].apply(lambda x : x.hour)

# for dayofweek column
data['DayofWeek'] = data['timeStamp'].apply(lambda x : x.dayofweek)

# for month column
data['month'] = data['timeStamp'].apply(lambda x : x.month)

# converting the dayofweek in string from dict
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
data['DayofWeek'] = data['DayofWeek'].map(dmap)


# contplot based day week column with reason

# sns.countplot(x='DayofWeek',hue='reason',data=data)

# count per-month
# sns.countplot(x='month',hue='reason',data=data)
# plt.legend(bbox_to_anchor = (1.05,1),loc=2,borderaxespad=0.)
# plt.show()

# countplot for each date
data['date'] = data['timeStamp'].apply(lambda x : x.date())

bydate = data.groupby('date').count()['lat']

# plot by reason
data[data['reason']=='EMS'].groupby('date').count()['twp'].plot()
# sns.countplot(x=data.groupby('reason').get_group('EMS').twp,data=data.groupby('reason').get_group('EMS'))
# print(data.groupby('reason').get_group('EMS'))
# sns.countplot(x='date',data=bydate.reset_index())
# bydate.plot()



# creating heat map

a = data.groupby(['DayofWeek','hour']).count()['reason'].unstack()
print(a)
sns.heatmap(a,cmap='magma',linecolor='white',linewidths=1)
# plt.xticks(rotation = 90)
plt.tight_layout()
plt.show()




