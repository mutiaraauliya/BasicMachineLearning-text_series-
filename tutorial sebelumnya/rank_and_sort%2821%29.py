
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1 = Series(range(3),index=['C','A','B'])
ser1


# In[2]:

ser1.sort_index()


# In[3]:

ser1.order()


# In[4]:

from numpy.random import randn
ser2 = Series(randn(10))
ser2


# In[6]:

ser2.sort(inplace=True)


# In[7]:

ser2.rank()


# In[8]:

ser3 = Series(randn(10))
ser3


# In[9]:

ser3.rank()


# In[ ]:



