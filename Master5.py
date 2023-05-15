#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd

df = pd.read_csv('api_dp_p1.csv')


# In[2]:


df.head()


# In[3]:


df.isnull().sum()


# In[4]:


(df.isnull().sum()/df.shape[0])*100


# In[5]:


df.drop(['product.manufacturer'],axis = 1, inplace = True)
df.drop(['product.sizes'],axis = 1, inplace = True)
df.drop(['product.weight'],axis = 1, inplace = True)

#for dropping columns if the null values percentage passess 50
# loop through the columns of the dataframe
#--for col in df.columns:
  # calculate the percentage of null values in the column
  #--null_percentage = df[col].isnull().sum() / df.shape[0] * 100
  # if the percentage is greater than 50%, drop the column
  #--if null_percentage > 50:
    #--df = df.drop(col, axis=1)
# print the updated dataframe
#--df


# In[6]:


df.columns


# In[7]:


duplicate = df[df.duplicated()]

duplicate


# In[8]:


df1 = df[['order.customer.customer_name']].copy()


# In[9]:


df1['First_Name'] = [fn.split()[0] for fn in df['order.customer.customer_name']] 
df1['LastName'] = [ln.split()[1] for ln in df['order.customer.customer_name']] 


# In[10]:


df1 


# In[11]:


df1[df1["First_Name"] == 'Alan'].nunique()


# In[12]:


df2 = df[['order.order_id','order.customer.customer_name','order.order_purchase_date']].copy()


# In[13]:


df2['order.order_purchase_date'] = pd.to_datetime(df2['order.order_purchase_date'])


# In[14]:


df2['day_of_order'] = df2['order.order_purchase_date'].dt.day_name()
df2


# In[15]:


import numpy as np


# In[16]:


df2['day_label'] = np.where(df2['order.order_purchase_date'].dt.dayofweek > 4,'Weekend', 'Weekday')


# In[17]:


df2.head()


# In[18]:


df2.where(df2['day_label'] == 'Weekend').nunique()


# In[19]:


df2['Sales'] = df['sales_amt']


# In[20]:


df2


# In[33]:


#df3 = df2.loc[(df2['day_label'] == 'Weekend')]
df3 = df2[df2['day_label'] == 'Weekend']


# In[34]:


df3['Sales'].sum()


# In[23]:


df3['Sales'].max()


# In[35]:


#df4 = df2.loc[(df2['day_label'] == 'Weekday')]
df4 = df2[df2['day_label'] == 'Weekday']


# In[36]:


df4['Sales'].sum()


# In[26]:


df4['Sales'].max()


# In[27]:


df2['Category'] = df[['product.category']].copy()


# In[28]:


df2.head()


# In[29]:


df5 = df2.groupby('Category')['Sales'].sum()


# In[30]:


df5


# In[ ]:




