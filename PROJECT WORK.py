#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install yfinance ')
# import pandas as pd


# In[18]:


get_ipython().system('pip install yfinance==0.2.4')
get_ipython().system('pip install pandas==1.3.3')


# # Using yfinance to Extract Tesla Stock Data

# In[6]:


import yfinance as yf
import pandas as pd


# In[7]:


tesla=yf.Ticker("TSLA")


# In[8]:


tesla_data=tesla.history(period="max")


# In[9]:


tesla_data.reset_index(inplace=True)
tesla_data.head()


# # Using YFinance to Extract GME Stock Data

# In[26]:


import yfinance as yf
import pandas as pd


# In[27]:


gme=yf.Ticker("GME")


# In[28]:


gme_data=gme.history(period="max")


# In[29]:


gme_data.reset_index(inplace=True)
gme_data.head()


# # Use Webscraping to Extract Tesla Revenue Data

# In[6]:


get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text


# In[17]:


soup = BeautifulSoup(html_data, "html5lib")
print(soup.prettify())


# In[5]:


tesla_revenue = pd.DataFrame(columns = ["Date","Revenue"])

for table in soup.find_all('table'):
    if table.find('th').getText().startswith("Tesla Quarterly Revenue"):
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) != 2: continue
            Date = col[0].text
            Revenue = col[1].text.replace("$","").replace(",","")
               
            tesla_revenue = tesla_revenue.append({"Date":Date, "Revenue":Revenue}, ignore_index=True)


# In[22]:


tesla_revenue.dropna(axis=0, how='all', subset=['Revenue']) #drop NaN values
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""] #drop empty string values


# In[23]:


tesla_revenue.tail(5)


# <!-- using yfinance to GME revenue data -->

# # Using webscraping to extract GME revenue data
# 

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[34]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text


# In[35]:


soup = BeautifulSoup(html_data, "html5lib")
print(soup.prettify())


# In[36]:


gme_revenue = pd.DataFrame(columns = ["Date","Revenue"])

for table in soup.find_all('table'):
    if table.find('th').getText().startswith("GameStop Quarterly Revenue"):
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) != 2: continue
            Date = col[0].text
            Revenue = col[1].text.replace("$","").replace(",","")
               
            gme_revenue = gme_revenue.append({"Date":Date, "Revenue":Revenue}, ignore_index=True)


# In[37]:


gme_revenue.tail(5)


# #  Plot Tesla Stock Graph

# In[8]:


get_ipython().system('pip install matplotlib')


# In[15]:


import matplotlib.pyplot as plt


# In[16]:


make_graph(tesla_data, tesla_revenue, 'Tesla')


# # Plot GameStop Stock Graph
# 

# In[ ]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




