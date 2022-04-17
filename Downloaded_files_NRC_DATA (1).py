#!/usr/bin/env python
# coding: utf-8

# Title:Downloading NRC Data
# Name:Ramandeep Kaur Bagri (rbagri@ucsc.edu)
# About Data: This file is created to download the NRC data in below link and format it specific order. 
# Data Link (Yet only one sample date, but links are avilbe to repeat the procedure): 
# https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041231ps.html#r3

# In[120]:


from bs4 import BeautifulSoup
import urllib.request as urllib2

url = "https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2000/index.html"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
headings = soup.findAll('h2');


# In[2]:


months=soup.find_all("h2")
dict1={}
main_url="https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004"
for month in months:
    dict1[month.text]=[main_url+"/"+link['href'].replace("2000","2004") for link in month.find_next("p").find_all("a")]


# In[3]:


dict1


# In[4]:


dict1.keys()


# In[70]:


import pandas as pd
df31_12_r1 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041231ps.html#r1')[0]


# In[71]:


import pandas as pd
df31_12_r2 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041231ps.html#r2')[1]


# In[72]:


import pandas as pd
df31_12_r3 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041231ps.html#r3')[2]


# In[73]:


import pandas as pd
df31_12_r4 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041231ps.html#r4')[3]


# In[119]:


url = 'https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041231ps.html'
dfs = pd.read_html(url)

df1 = dfs[0]
df2 = dfs[1]
df3 = dfs[2]
df4 = dfs[3]

#index_col = 0, date_parser = lambda time: pd.Timestamp('2013/02/01 %s' % time)

df1 = df1.drop(columns=['Down','Reason or Comment', 'Change in report (*)','Number of Scrams (#)'])
df2 = df2.drop(columns=['Down','Reason or Comment', 'Change in report (*)','Number of Scrams (#)'])
df3 = df3.drop(columns=['Down','Reason or Comment', 'Change in report (*)','Number of Scrams (#)'])
df4 = df4.drop(columns=['Down','Reason or Comment', 'Change in report (*)','Number of Scrams (#)'])

frames = [df1, df2, df3, df4]
result = pd.concat(frames)

print (df1.head())
print (df2.head())
print (df3.head())
print (df4.head())
print (result.head())

print (len(df1))
print (len(df2))
print (len(df3))
print (len(df4))
print (len(result))

result['ReportDt'] = pd.date_range(start='12/31/2004', end='12/31/2004', periods=len(result))

columnsTitles = ['ReportDt', 'Unit', 'Power']

result = result.reindex(columns=columnsTitles)
print (result.head())

result.to_csv('dec312004file.txt', sep='|', index=False)


# In[65]:


df31_12_r1.head()


# In[66]:


df31_12_r2.head()


# In[67]:


df31_12_r3.head()


# In[68]:


df31_12_r3.head()


# In[69]:


df31_12_r4.head()


# In[32]:


import pandas as pd
df31_2 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041230ps.html#r2')[0]


# In[33]:


df13=df31_2.drop(columns=['Down','Reason or Comment', 'Change in report (*)','Number of Scrams (#)' ])
df13.head()


# In[34]:


df13


# In[16]:


#downloading data from each page of month december 
df31_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041231ps.html')
df30_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041230ps.html')
df29_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041229ps.html')
df28_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041228ps.html')
df27_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041227ps.html')
df26_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041226ps.html')
df25_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041225ps.html')
df24_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041224ps.html')
df23_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041223ps.html')
df22_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041222ps.html')
df21_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041221ps.html')
df20_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041220ps.html')
df19_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041219ps.html')
df18_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041218ps.html')
df17_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041217ps.html')
df16_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041216ps.html')
df15_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041215ps.html')
df14_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041214ps.html')
df13_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041213ps.html')
df12_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041212ps.html')
df11_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041211ps.html')
df10_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041210ps.html')
df09_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041209ps.html')
df08_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041208ps.html')
df07_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041207ps.html')
df06_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041206ps.html')
df05_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041205ps.html')
df04_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041204ps.html')
df03_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041203ps.html')
df02_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041202ps.html')
df01_12 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041201ps.html')


# In[17]:


#downloading data from each page of month november
df30_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041130ps.html')
df29_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041129ps.html')
df28_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041128ps.html')
df27_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041127ps.html')
df26_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041126ps.html')
df25_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041125ps.html')
df24_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041124ps.html')
df23_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041123ps.html')
df22_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041122ps.html')
df21_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041121ps.html')
df20_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041120ps.html')
df19_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041119ps.html')
df18_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041118ps.html')
df17_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041117ps.html')
df16_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041116ps.html')
df15_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041115ps.html')
df14_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041114ps.html')
df13_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041113ps.html')
df12_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041112ps.html')
df11_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041111ps.html')
df10_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041110ps.html')
df09_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041109ps.html')
df08_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041108ps.html')
df07_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041107ps.html')
df05_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041105ps.html')
df04_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041104ps.html')
df03_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041103ps.html')
df02_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041102ps.html')
df01_11 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041101ps.html')


# In[18]:


#downloading data from each page of month oct
df31_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041031ps.html')
df30_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041030ps.html')
df29_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041029ps.html')
df28_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041028ps.html')
df27_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041027ps.html')
df26_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041026ps.html')
df25_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041025ps.html')
df24_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041024ps.html')
df23_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041023ps.html')
df22_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041022ps.html')
df21_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041021ps.html')
df20_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041020ps.html')
df19_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041019ps.html')
df18_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041018ps.html')
df17_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041017ps.html')
df16_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041016ps.html')
df15_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041015ps.html')
df14_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041014ps.html')
df13_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041013ps.html')
df12_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041012ps.html')
df10_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041010ps.html')
df09_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041009ps.html')
df08_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041008ps.html')
df07_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041007ps.html')
df06_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041006ps.html')
df05_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041005ps.html')
df04_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041004ps.html')
df03_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041003ps.html')
df02_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041002ps.html')
df01_10 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20041001ps.html')
 


# In[19]:


#downloading data from each page of month September
df30_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040930ps.html')
df29_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040929ps.html')
df28_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040928ps.html')
df27_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040927ps.html')
df26_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040926ps.html')
df25_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040925ps.html')
df24_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040924ps.html')
df23_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040923ps.html')
df22_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040922ps.html')
df21_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040921ps.html')
df20_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040920ps.html')
df19_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040919ps.html')
df18_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040918ps.html')
df17_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040917ps.html')
df16_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040916ps.html')
df15_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040915ps.html')
df14_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040914ps.html')
df13_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040913ps.html')
df11_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040911ps.html')
df10_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040910ps.html')
df09_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040909ps.html')
df08_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040908ps.html')
df07_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040907ps.html')
df06_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040906ps.html')
df05_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040905ps.html')
df04_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040904ps.html')
df03_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040903ps.html')
df02_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040902ps.html')
df01_09 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040901ps.html')


# In[20]:


#downloading data from each page of month 'August'
df31_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040831ps.html',
df30_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040830ps.html',
df29_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040829ps.html',
df28_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040828ps.html',
df27_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040827ps.html',
df26_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040826ps.html',
df25_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040825ps.html',
df24_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040824ps.html',
df23_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040823ps.html',
df22_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040822ps.html',
df21_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040821ps.html',
df20_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040820ps.html',
df19_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040819ps.html',
df18_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040818ps.html',
df17_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040817ps.html',
df16_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040816ps.html',
df15_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040815ps.html',
df14_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040814ps.html',
df13_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040813ps.html',
df12_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040812ps.html',
df11_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040811ps.html',
df10_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040810ps.html',
df09_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040809ps.html',
df08_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040808ps.html',
df07_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040807ps.html',
df06_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040806ps.html',
df05_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040805ps.html',
df04_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040804ps.html',
df03_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040803ps.html',
df02_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040802ps.html',
df01_08 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040801ps.html']


# In[ ]:


#downloading data from each page of month 'July'
df31_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040731ps.html')
df30_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040730ps.html')
df29_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040729ps.html')
df28_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040728ps.html')
df27_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040727ps.html')
df26_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040726ps.html')
df25_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040725ps.html')
df24_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040724ps.html')
df23_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040723ps.html')
df22_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040722ps.html')
df21_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040721ps.html')
df20_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040720ps.html')
df19_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040719ps.html')
df18_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040718ps.html')
df17_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040717ps.html')
df16_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040716ps.html')
df15_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040715ps.html')
df14_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040714ps.html')
df13_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040713ps.html')
df12_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040712ps.html')
df11_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040711ps.html')
df10_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040710ps.html')
df09_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040709ps.html')
df08_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040708ps.html')
df07_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040707ps.html')
df06_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040706ps.html')
df05_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040705ps.html')
df04_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040704ps.html')
df03_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040703ps.html')
df02_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040702ps.html')
df01_07 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040701ps.html')
 


# In[ ]:


#downloading data from each page of month 'June'
df30_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040630ps.html')
df29_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040629ps.html')
df28_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040628ps.html')
df27_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040627ps.html')
df26_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040626ps.html')
df25_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040625ps.html')
df24_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040624ps.html')
df23_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040623ps.html')
df22_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040622ps.html')
df21_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040621ps.html')
df20_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040620ps.html')
df19_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040619ps.html')
df18_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040618ps.html')
df17_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040617ps.html')
df16_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040616ps.html')
df15_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040615ps.html')
df14_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040614ps.html')
df13_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040613ps.html')
df12_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040612ps.html')
df11_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040611ps.html')
df10_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040610ps.html')
df09_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040609ps.html')
df08_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040608ps.html')
df07_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040607ps.html')
df06_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040606ps.html')
df05_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040605ps.html')
df04_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040604ps.html')
df03_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040603ps.html')
df02_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040602ps.html')
df01_06 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040601ps.html')
 


# In[ ]:


#downloading data from each page of month 'May'
df31_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040531ps.html')
df30_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040530ps.html')
df29_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040529ps.html')
df28_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040528ps.html')
df27_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040527ps.html')
df26_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040526ps.html')
df25_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040525ps.html')
df24_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040524ps.html')
df23_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040523ps.html')
df22_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040522ps.html')
df21_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040521ps.html')
df20_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040520ps.html')
df19_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040519ps.html')
df18_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040518ps.html')
df17_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040517ps.html')
df16_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040516ps.html')
df15_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040515ps.html')
df14_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040514ps.html')
df13_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040513ps.html')
df12_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040512ps.html')
df11_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040511ps.html')
df10_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040510ps.html')
df09_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040509ps.html')
df08_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040508ps.html')
df07_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040507ps.html')
df06_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040506ps.html')
df05_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040505ps.html')
df04_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040504ps.html')
df03_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040503ps.html')
df02_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040502ps.html')
df01_05 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040501ps.html')


# In[ ]:


#downloading data from each page of month 'April'
df30_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040430ps.html')
df29_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040429ps.html')
df28_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040428ps.html')
df27_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040427ps.html')
df26_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040426ps.html')
df25_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040425ps.html')
df24_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040424ps.html')
df23_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040423ps.html')
df22_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040422ps.html')
df21_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040421ps.html')
df20_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040420ps.html')
df19_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040419ps.html')
df18_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040418ps.html')
df17_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040417ps.html')
df16_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040416ps.html')
df15_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040415ps.html')
df14_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040414ps.html')
df13_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040413ps.html')
df12_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040412ps.html')
df11_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040411ps.html')
df10_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040410ps.html')
df09_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040409ps.html')
df08_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040408ps.html')
df07_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040407ps.html')
df06_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040406ps.html')
df05_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040405ps.html')
df04_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040404ps.html')
df03_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040403ps.html')
df02_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040402ps.html')
df01_04 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040401ps.html')


# In[ ]:


#downloading data from each page of month 'March'
df31_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040331ps.html')
df30_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040330ps.html')
df29_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040329ps.html')
df28_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040328ps.html')
df27_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040327ps.html')
df26_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040326ps.html')
df25_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040325ps.html')
df24_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040324ps.html')
df23_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040323ps.html')
df22_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040322ps.html')
df21_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040321ps.html')
df20_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040320ps.html')
df19_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040319ps.html')
df18_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040318ps.html')
df17_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040317ps.html')
df16_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040316ps.html')
df15_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040315ps.html')
df14_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040314ps.html')
df13_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040313ps.html')
df12_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040312ps.html')
df11_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040311ps.html')
df10_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040310ps.html')
df09_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040309ps.html')
df08_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040308ps.html')
df07_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040307ps.html')
df06_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040306ps.html')
df05_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040305ps.html')
df04_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040304ps.html')
df03_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040303ps.html')
df02_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040302ps.html')
df01_03 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040301ps.html')


# In[ ]:


#downloading data from each page of month'February'
df29_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040229ps.html')
df28_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040228ps.html')
df27_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040227ps.html')
df26_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040226ps.html')
df25_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040225ps.html')
df24_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040224ps.html')
df23_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040223ps.html')
df22_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040222ps.html')
df21_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040221ps.html')
df20_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040220ps.html')
df19_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040219ps.html')
df18_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040218ps.html')
df17_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040217ps.html')
df16_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040216ps.html')
df15_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040215ps.html')
df14_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040214ps.html')
df13_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040213ps.html')
df12_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040212ps.html')
df11_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040211ps.html')
df10_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040210ps.html')
df09_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040209ps.html')
df08_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040208ps.html')
df07_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040207ps.html')
df06_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040206ps.html')
df05_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040205ps.html')
df04_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040204ps.html')
df03_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040203ps.html')
df02_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040202ps.html')
df01_02 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040201ps.html')
 


# In[ ]:


#downloading data from each page of month'January'
df31_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040131ps.html')
df30_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040130ps.html')
df29_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040129ps.html')
df28_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040128ps.html')
df27_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040127ps.html')
df26_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040126ps.html')
df25_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040125ps.html')
df24_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040124ps.html')
df23_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040123ps.html')
df22_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040122ps.html')
df21_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040121ps.html')
df20_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040120ps.html')
df19_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040119ps.html')
df18_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040118ps.html')
df17_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040117ps.html')
df16_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040116ps.html')
df15_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040115ps.html')
df14_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040114ps.html')
df13_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040113ps.html')
df12_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040112ps.html')
df11_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040111ps.html')
df10_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040110ps.html')
df09_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040109ps.html')
df08_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040108ps.html')
df07_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040107ps.html')
df06_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040106ps.html')
df05_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040105ps.html')
df04_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040104ps.html')
df03_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040103ps.html')
df02_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040102ps.html')
df01_01 = pd.read_html('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2004/20040101ps.html')
 


# In[ ]:


# METHOD 2
for November in dict1.keys():
    print(November, '-->', dict1[November])


# In[ ]:




