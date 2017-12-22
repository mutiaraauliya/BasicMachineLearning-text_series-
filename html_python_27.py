
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
#pip install beautiful-soup
#pip install html5lib

dframe_list = pd.io.html.read_html(url)
dframe = dframe_list[0]
dframe


# In[2]:

dframe.columns.values


# In[ ]:



