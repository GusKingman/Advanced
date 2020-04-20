#!/usr/bin/env python
# coding: utf-8

# In[90]:


import requests #library used to download web pages.


# In[91]:


#specify the url
URL = "https://en.wikipedia.org/wiki/List_of_counties_in_Maryland#List_of_counties"


# In[92]:


#page is the variable being created for the URL
#get lets it know we are going to request data 
page = requests.get(URL)


# In[93]:


type(page)
#want response


# In[94]:


#get 200 means good
page.status_code


# In[95]:


#save stringof website HTML into a variable calle HTMLstr
#prints the first 300 characters to see what it looks like
#300 is arbitrary 
HTMLstr = page.text
print(HTMLstr[:300])


# In[96]:


#soup time
from bs4 import BeautifulSoup


# In[97]:


# parse the html using beautiful soup, store as soup
#HTMLstr means its raw HTML content.
#html.parser is Specifying the HTML parser we want to use.
soup = BeautifulSoup(HTMLstr, "html.parser")


# In[98]:


#see what it looks like
soup


# In[99]:


#cleans it nicely
print (soup.prettify())


# In[100]:


soup.title


# In[101]:


#print it for fun
print(soup.title.string)


# In[ ]:





# In[ ]:





# In[102]:


#okie dokkie , table in page it is a wikitable sortable
# get the <table> tag that contains the data we want to scrape

County_table=soup.find('table', class_='wikitable sortable')
County_table


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#soup.find_all("a")


# In[ ]:


#show hyperlink reference for all <a> tags
#all_links=soup.find_all("a")

#for link in all_links:
  #  print (link.get("href"))


# In[ ]:


#find all the <table> tags 
#all_tables=soup.find_all('table')
#all_tables


# In[ ]:





# In[ ]:





# In[ ]:





# In[119]:


#set empty lists to hold data of each column
X=[]#blank
A=[]# county 
#B=[]# fips code
#C=[]# county seat
D=[]# established
E=[]#origin 
F=[]#et
#G=[]#flag
#H=[]#seal
I=[]#pop
J=[]#area
#K=[]#map


for row in County_table.findAll("tr"):
    #ounty names were table heads
    heads = row.findAll("th")
    cells = row.findAll('td')
    
    if len(cells)==10: 
        
        A.append(heads[0].find(text=True)) #gets info in county column and adds it to list A
        D.append(cells[2].find(text=True)) # gets info from est column and adds it to list D
        E.append(cells[3].find(text=True)) # gets info from origin solumn and adds it to list E
        F.append(cells[4].find(text=True)) # gets info from ety column and adds it to list F
        I.append(cells[7].find(text=True)) # gets info from pop column and adds it to list I
        J.append(cells[8].find(text=True)) # gets info from area column and adds it to list J


# In[ ]:





# In[120]:


#verify data in list A (county)
F


# In[121]:


#import pandas to convert list to data frame
import pandas as pd


# In[122]:


df=pd.DataFrame(A, columns=['County'])


# In[123]:


#add other lists as new columns in my new dataframe
#df[''] = B
#df['Statehood'] = C
df['established'] = D
df['origin'] = E
df['etymology'] = F
#df['Municipal'] = G
#df['Metropolitan'] = H
df['population'] = I
df['area'] = J
#df['Notes'] = K


# In[124]:


df.head()


# In[ ]:


#export
df.to_csv("County.csv")

