
# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

ser1 = Series(np.arange(3),index=['a','b','c'])
ser1


# In[5]:

ser1.drop('b')


# In[8]:

dframe1 = DataFrame(np.arange(9).reshape((3,3)),index=['SF','NY','LA'],columns=['pop','size','year'])


# In[9]:

dframe1


# In[10]:

dframe1.drop('LA')


# In[11]:

dframe2 = dframe1.drop('LA')
dframe2


# In[12]:

dframe1.drop('year',axis=1)


# In[ ]:



