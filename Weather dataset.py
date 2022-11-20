#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv(r'D:\python docouments\analytics_dataset\Weather Data.csv')


# In[3]:


data.head(2)


# ## Data Exploration

# In[4]:


data.head(2)


# In[5]:


data.shape


# In[6]:


data.index


# In[7]:


data.columns


# In[8]:


data['Weather'].unique()


# In[9]:


data.nunique()


# In[10]:


data.count()


# In[11]:


data['Weather'].count()


# In[12]:


data['Weather'].value_counts()


# ## Find all the unique 'wind speed' values in the data

# In[13]:


data.head(2)


# In[14]:


data['Wind Speed_km/h'].nunique()


# ## find the number of times when the weather is exactly clear

# In[15]:


data.head(2)


# In[16]:


data['Weather'].value_counts() ## method 1


# In[17]:


data[data['Weather'] == "Clear"] ## method 2


# In[18]:


data.groupby('Weather').get_group('Clear') ## method 3


# ## find the number of times when ' wind speed' was exactly 4 km/hr

# In[19]:


data.head(2)


# In[20]:


data[data['Wind Speed_km/h'] == 4] ##  filtering method


# ## find all the null values in the data

# In[21]:


data.isnull().sum()


# ## rename the column name 'weather' of the dataframe to 'weather condition'

# In[22]:


data.head(1)


# In[23]:


data.rename(columns = {'Weather': 'Weather Condition'}, inplace = True)


# In[24]:


data.head(1)


# ## what is the mean 'visibility'?

# In[25]:


data['Visibility_km'].mean()


# ## what is the Standard deviation of pressure in this data?

# In[26]:


data.head(1)


# In[27]:


data['Press_kPa'].std()


# ## what is the variance of relative humidity in this data?
# 

# In[28]:


data['Rel Hum_%'].var()


# ## find all the instances when the snow was recoreded

# In[29]:


data.head(1)


# In[30]:


data[data['Weather Condition'].str.contains('Snow')]


# ## find all the instances when 'wind speed is above 24' and 'visibility is 25'

# In[31]:


data.head(1)


# In[32]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# ## what is the mean value of each column against each 'weather condition'?

# In[33]:


data.head(1)


# In[34]:


data.groupby('Weather Condition').mean()


# ## what is the minimum and maximum value of each column against each weather condition?

# In[35]:


data.head(1)


# In[36]:


data.groupby('Weather Condition').min()


# In[37]:


data.groupby('Weather Condition').max()


# ## show all the records where weather conditon is FOG

# In[38]:


data.head(1)


# In[39]:


data[data['Weather Condition'] == 'Fog']


# ## Find all the instances when 'weather is clear' or 'visibility is above 40'

# In[40]:


data.head(1)


# In[41]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]


# ## find all the instances when 
#     weather is clear and relative humidity is greater than 50 or 
#     visibility is above 40

# In[42]:


data.head(1)


# In[43]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)| (data['Visibility_km'] > 40)]


# In[ ]:




