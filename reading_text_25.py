
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dframe = pd.read_csv('/home/mutiaraauliya/text_series_ML/teks.csv')
dframe


# In[4]:

dframe = pd.read_csv('/home/mutiaraauliya/text_series_ML/teks.csv',header = None)
dframe


# In[5]:

dframe = pd.read_table('/home/mutiaraauliya/text_series_ML/teks.csv',sep=',',header=None)
dframe


# In[6]:

pd.read_csv('/home/mutiaraauliya/text_series_ML/teks.csv',header=None,nrows=2)


# In[8]:

dframe


# In[9]:

#untuk import file csv nyaa
dframe.to_csv('/home/mutiaraauliya/text_series_ML/teksdataoutput.csv')


# In[10]:

import sys
dframe.to_csv(sys.stdout)


# In[11]:

dframe.to_csv(sys.stdout,sep='_')


# In[13]:

dframe.to_csv(sys.stdout,columns=[0,1,2])


# In[15]:

url ='https://docs.python.org/2/library/csv.html'
url


# In[ ]:



