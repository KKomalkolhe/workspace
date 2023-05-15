#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import pandas as pd
base_url = "https://globalmart-api.onrender.com"
endpoint = "/mentorskool/v1/sales?offset=1&limit=100"
headers = {"access_token": "fe66583bfe5185048c66571293e0d358"}
url = base_url + endpoint
final_list = []
nxt = ""
for i in range(5):
    if nxt != "":
        url = base_url + nxt
    response = requests.get(url, headers = headers)
    data = response.json()["data"]
    nxt = response.json()["next"]
    final_list.extend(data)
df = pd.json_normalize(final_list)
df.to_csv('master14.csv', index = False)


# In[ ]:




