#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import pandas as pd

url = "https://globalmart-api.onrender.com/mentorskool/v1/sales?offset=1&limit=100"
headers = {"access_token": "fe66583bfe5185048c66571293e0d358"}

response = requests.get(url)

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)


# In[ ]:




