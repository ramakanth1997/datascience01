#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
d=pd.read_excel("C:\\Users\\006595\\Downloads\\world_economic_data.xlsx")
df=pd.DataFrame(d)   


# In[10]:


df_1=df.describe()
df_1


# In[11]:


df_2=df.head()
df_2


# In[12]:


df_3=df.tail()
df_3


# In[13]:


df_4=df_1.shape
df_4


# In[14]:


df_6=df.sort_values("Units")
df_6


# In[15]:


df_7=df.sort_values(["Country","Units"])
df_7


# In[16]:


df_8=df.groupby(['Country'])[['Subject Descriptor','Units']].count()
df_8


# In[17]:


df_9=df.groupby(['Country'])['Subject Descriptor','Units'].agg(['max','min'])
df_9


# In[18]:


df_10=df[(df['Subject Descriptor']=='Current account balance')&(df['Units']=='U.S. dollars')]
df_10


# In[19]:


df_11=df[(df['Country']=='Bangladesh')&(df['Units']=='U.S. dollars')]
df_11


# In[20]:


df_11=df[(df['Country']=='Bangladesh')&(df['Units']=='Percent of GDP')]
df_11


# In[21]:


df_12=df[(df['Country']=='Bangladesh')&(df['Subject Descriptor']!='Total investment')]
df_12


# In[22]:


df_13=df[(df['Units']=='Volume of imports of goods and services')&(df['Country']=='India')].count()
df_13


# In[23]:


df_14=df.loc[6]

df_14


# In[24]:


df_15=df[(df['Country']=='India')&(df['Subject Descriptor']!='Population')]
df_15


# In[25]:


df_16=df.loc[6 :50]!='Population'

df_16


# In[26]:


df_17=df[(df['Subject Descriptor']=='Population')&(df['Estimates Start After']==2020)]
df_17


# In[27]:


df_18=df.groupby([1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,"Country"]).count()
df_18


# In[28]:


df_19=df.groupby([1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,"Subject Descriptor"]).count()
df_19


# In[29]:


df_20=df.groupby([1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,"Country"]).agg('max')
df_20


# In[30]:


df_21=df.groupby([1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,"Country","Subject Descriptor"]).agg('min')
df_21


# In[31]:


df_22=df.groupby(["Country","Subject Descriptor","Scale",1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022][0]).agg('max')
df_22

#It shows the Maximum value in the Country 


# In[32]:


df_23=df.groupby(["Country","Subject Descriptor","Scale",1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022][0]).agg('min')
df_23

#It shows the Minimum value in the country in Index values which can be consider from units and 1980 coloumn 


# In[33]:


df_24=df.groupby(["Country","Subject Descriptor","Scale",1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]).agg('min')
df_24

#It shows the Minimum value in the country


# In[34]:


df_25=df.groupby(["Country","Subject Descriptor","Scale",1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022][3]).agg('min')
df_25

#It shows the Minimum value to maximum in the country in 1980 coloumn


# In[36]:


df_26=df.groupby(["Country","Subject Descriptor","Scale",1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022][0]).count()
df_26


# In[ ]:




