
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
json_obj = """
{   "zoo_animal": "Lion",
    "food": ["Meat", "Veggies", "Honey"],
    "fur": "Golden",
    "clothes": null, 
    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
}
"""
import json 
data = json.loads(json_obj)
data


# In[2]:

json.dumps(data)


# In[4]:

dframe = DataFrame(data['diet'])
dframe


# In[ ]:



