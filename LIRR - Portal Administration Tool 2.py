#!/usr/bin/env python
# coding: utf-8

# # Generates portal insights for the administrator to use for mintne

# # Connect to pandas & explore data

# In[1]:


# Import pandas
import pandas as pd


# In[2]:


# Connect to file
df = pd.read_excel (r'C:\Users\JosePillich\Desktop\lirr\Mapping_Portals\Tool\ArcGis_Online_Group_Audit_QAItemAudit.xls')


# In[3]:


# Show all columns
df.columns


# In[4]:


# Checking the structure of the data 
df.head()


# # Select columns from DF, group variables and export to .txt/.csv

# # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# In[16]:


# Selecting columns from spreadsheet df[['GroupTitle', 'ItemTitle', 'ItemType','ItemNumViews']]
df[['GroupTitle', 'ItemTitle', 'ItemType','ItemNumViews']]



# In[17]:


# Selecting columns from spreadsheet 
df = df[['GroupTitle', 'ItemTitle', 'ItemType','ItemNumViews']]


# In[18]:


# Convert dataframe to CSV
df.to_csv('Group_MetaData1.csv')


# In[19]:


# Convert dataframe to CSV
df.to_csv('Group_MetaData1.txt')


# # Grouping variables by Service Layer

# # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# In[9]:


# grouping the data
group = data.groupby('ItemTitle')['ItemType']


# In[ ]:


# total number appears in 
group_count = group.count()
print(group_count)


# In[ ]:





# In[ ]:





# In[21]:


from noaa_sdk import noaa
n = noaa.NOAA()
res = n.get_forecasts('11365', 'US', True)
for i in res:
    print(i)


# In[25]:


print(res)


# In[26]:


test


# In[27]:


x = 2 


# In[28]:


print(x)


# In[ ]:




