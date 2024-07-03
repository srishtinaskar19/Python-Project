#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('iris.csv')
df.head()


# # 2

# In[2]:


import pandas as pd


print(df.head(8))


# In[ ]:





# # 3

# In[3]:


df = pd.read_csv('iris.csv')


odd_numbered_rows = df.iloc[1::2]


shuffled_rows = odd_numbered_rows.sample(frac=1)

print(shuffled_rows)


# # 4

# In[4]:


df = pd.read_csv('iris.csv')  


num_columns = df.shape[1]
print(f"Number of columns: {num_columns}")


column_names = df.columns
print("Column names:")
for name in column_names:
    print(name)


# # 5

# In[5]:


df.shape


# # 6

# In[6]:


import pandas as pd


df = pd.read_csv('iris.csv')  

sliced_data = df.iloc[10:20, [0, 2, 5]]  

print("Sliced dataset:")
print(sliced_data)


# # 7

# In[7]:


print(df.loc[:,df.columns.str.startswith('Petal Width')])


# # 8

# In[8]:


df.loc[0]


# In[9]:


df.iloc[3]


# # 9

# In[11]:


df = pd.read_csv('iris.csv')  


num_columns = df.shape[1]
print(f"Number of columns: {num_columns}")


column_names = df.columns
print("Column names:")
for name in column_names:
    print(name)


# In[ ]:




