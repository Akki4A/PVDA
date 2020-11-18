#!/usr/bin/env python
# coding: utf-8

# # Personal Data Analyzer: Netflix

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('ViewingActivity.csv')


# In[3]:


df.shape


# In[4]:


df.head(2)


# In[5]:


df = df.drop(['Profile Name','Attributes','Supplemental Video Type','Device Type','Bookmark','Latest Bookmark','Country'], axis = 1)
df.head(2)


# In[6]:


df.dtypes


# In[7]:


df['Start Time'] = pd.to_datetime(df['Start Time'], utc = True)
df.dtypes


# In[8]:


# change the Start Time column into the dataframe's index
df = df.set_index('Start Time')

# convert from UTC timezone to Asian/Kolkata time
df.index = df.index.tz_convert('Asia/Kolkata')

# reset the index so that Start Time becomes a column again
df = df.reset_index()

#double-check that it worked
df.head(1)


# In[9]:


df.dtypes


# In[10]:


df['Duration'] = pd.to_timedelta(df['Duration'])
df.dtypes


# In[11]:


df.head(1)


# In[12]:


# create a new dataframe called star that that takes from df
# only the rows in which the Title column contains 'Friends'
star = df[df['Title'].str.contains('Friends', regex=False)]


# In[13]:


star.shape


# In[14]:


star = star[(star['Duration']> '0 days 00:01:00')]
star.shape


# # This is How Much Time i have spent watching Friends

# In[15]:


star['Duration'].sum()


# In[16]:


star['weekday'] = star['Start Time'].dt.weekday
star['hour'] = star['Start Time'].dt.hour

# check to make sure the columns were added correctly
star.head(1)


# # Graphical Representation:

# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


import matplotlib


# In[19]:


# set our categorical and define the order so the days are plotted Monday-Sunday
star['weekday'] = pd.Categorical(star['weekday'], categories=
    [0,1,2,3,4,5,6],
    ordered=True)

# create star_by_day and count the rows for each weekday, assigning the result to that variable
star_by_day = star['weekday'].value_counts()

# sort the index using our categorical, so that Monday (0) is first, Tuesday (1) is second, etc.
star_by_day = star_by_day.sort_index()

# optional: update the font size to make it a bit larger and easier to read
matplotlib.rcParams.update({'font.size': 16})


# plot star_by_day as a bar chart with the listed size and title
star_by_day.plot(kind='bar', figsize=(10,5), title='Friends Episodes Watched by Day by Akki4A', color=(0.4,0.2,0.6))


# In[20]:


# set our categorical and define the order so the hours are plotted 1-24 hours
star['hour'] = pd.Categorical(star['hour'], categories=
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
    ordered=True)

# create star_by_hour and count the rows for each hour, assigning the result to that variable
star_by_day = star['hour'].value_counts()

# sort the index using our categorical, so that 1 (0) is 1 hour, 2 (1) is 2 hour  so on...
star_by_day = star_by_day.sort_index()

matplotlib.rcParams.update({'font.size': 14})

star_by_day.plot(kind='bar', figsize=(10,5), title='Friends Episodes Watched by Hour by Akki4A', color=(0.4,0.2,0.6))


# In[ ]:





# In[ ]:




