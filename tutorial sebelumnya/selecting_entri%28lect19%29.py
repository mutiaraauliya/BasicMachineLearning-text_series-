
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

ser1 = Series(np.arange(3),index=['A','B','C'])


# In[5]:

ser1 = 2*ser1
ser1


# In[6]:

ser1['B']


# In[7]:

ser1[1]


# In[8]:

ser1[0:3]


# In[9]:

ser1[['A','B']]


# In[11]:

ser1[ser1>8]


# In[13]:

ser1[ser1>3] = 10
ser1


# In[17]:

dframe = DataFrame(np.arange(25).reshape((5,5)),index=['Adgard','Skrim','Turki','USA',"Indo"],columns=['a','b','c','d','e'])
dframe


# In[19]:

dframe['b']


# In[20]:

dframe > 10


# In[23]:

#satu kolom
dframe.ix['Indo']


# In[24]:

dframe.ix[1]


# In[ ]:



