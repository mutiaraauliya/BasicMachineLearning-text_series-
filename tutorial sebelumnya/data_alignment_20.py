
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

ser1 = Series([0,1,2],index=['A','B','C'])
ser1


# In[2]:

ser2 = Series([3,4,5,6],index=['A','B','C','D'])
ser2


# In[3]:

ser1+ser2


# In[4]:

dframe1 = DataFrame(np.arange(4).reshape((2,2)),columns=list('AB'),index=['skyrim','asgard'])
dframe1


# In[7]:

dframe2 = DataFrame(np.arange(9).reshape((3,3)),columns=list('ABC'),index=['skyrim','asgard','bumi'])
dframe2


# In[8]:

dframe1+dframe2


# In[9]:

dframe1


# In[12]:

dframe1.add(dframe2,fill_value=0)


# In[13]:

dframe1


# In[15]:

ser3 = dframe2.ix[0]
ser3


# In[16]:

dframe2-ser3


# In[ ]:



