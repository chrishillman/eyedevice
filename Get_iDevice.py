#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import urllib
import html5lib


# In[2]:


ideviceurl = "https://www.theiphonewiki.com/wiki/Models"


# In[33]:


html_table = urllib.request.urlopen(ideviceurl).read()

# fix HTML
soup = BeautifulSoup(html_table, "html.parser")
dflist = []
for table in soup.find_all("table", {"class": "wikitable"}):
    if table:
        try:
            thisdf = pd.read_html(str(table), flavor="bs4")[0]
            if thisdf['Identifier'][0] != 'Unknown':
                dflist.append(thisdf)
                print("dflist appended")
            else:
                print("Skipped")
        except Exception as e:
            print(f"ERROR: {e}")


# In[36]:


for df in dflist:
    print(df['Generation'][0])
    if df['Generation'][0] == '?':
        print(df)


# In[39]:


for devicedf in dflist:
    filename = "".join(devicedf['Generation'][0].split(" "))
    filename = filename.split("(")[0]
    filename = filename + ".csv"
    print(filename)
    devicedf.to_csv(filename)

