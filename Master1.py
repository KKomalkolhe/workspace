#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import pandas as pd

url = "https://globalmart-api.onrender.com/mentorskool/v1/sales?offset=1&limit=100"
headers = {"access_token": "fe66583bfe5185048c66571293e0d358"}

response = requests.get(url, headers = headers)

if response.status_code == 200:
    df = pd.json_normalize(response.json()['data'])
else:
    print("Request failed with status code: ", response.status_code)

df


# In[ ]:




