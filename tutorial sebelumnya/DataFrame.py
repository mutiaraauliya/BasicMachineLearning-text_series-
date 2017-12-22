
# coding: utf-8

# In[5]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import webbrowser as wb
website = wb.open = 'https://en.wikipedia.org/wiki/NFL_win-loss_records'
wb.get('firefox %s').open(website)


# untuk ngubah browsernya pake jupyter notebook --generate-config di terminal terus ubah webbrowsernya

# In[8]:

nfl_frame = pd.read_clipboard()
nfl_frame


# In[10]:

nfl_frame.columns


# In[23]:

nfl_frame.columns


# In[24]:

nfl_frame['Rank ']


# In[25]:

DataFrame(nfl_frame,columns=['Team ', 'First NFL Season ','Total Games '])


# In[26]:

DataFrame(nfl_frame,columns=['Team ', 'First NFL Season ','Total Games ','Stadium '])


# In[27]:

nfl_frame


# In[30]:

#2datapertama
nfl_frame.head(2)


# In[31]:

#3data terakhir
nfl_frame.tail(3)


# In[32]:

#mengikuti index
nfl_frame.ix[3]


# In[34]:

nfl_frame['Stadium '] = "Stadium A"
nfl_frame


# In[35]:

nfl_frame['Stadium '] = np.arange(10)
nfl_frame


# In[38]:

stadiums = Series(['Stadium A','Stadium B'],index=[9,0])
stadiums


# In[39]:

nfl_frame['Stadium '] = stadiums
nfl_frame


# In[40]:

#buat delete kolom
del nfl_frame['Stadium ']
nfl_frame


# In[41]:

data = {'City':['Klaten','Jogja','Solo'],'POpulasi':[87600,78300,39999]}
city_frame = DataFrame(data)
city_frame


# In[ ]:



