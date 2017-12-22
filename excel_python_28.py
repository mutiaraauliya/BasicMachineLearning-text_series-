
# coding: utf-8

# In[1]:

import pandas as pd

xlsfile = pd.ExcelFile('/home/mutiaraauliya/text_series_ML/excel.xls')
dframe = xlsfile.parse('Sheet1')
dframe


# In[ ]:



