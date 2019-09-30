
# coding: utf-8

# Задача 1

# In[62]:


import numpy as np
a= np.random.random((10,3))
b=a-[0.5,0.5,0.5]
c=np.min(abs(b)-0.5,axis=1)
print(c)


# Задача 2

# In[69]:



a= np.random.random((6,6))
b=a
np.transpose(b)
for i in range(6):
    print(a[i].sum()/b[i].max())


# Задача 3

# In[51]:



x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

mask= x==0
print (x[1:][mask[:-1]].max())



# Задача 4

# In[53]:



x = np.ones(10) 
i = np.array([0, 1, 2, 3, 5, 5, 5, 8])

x+=np.bincount(i,minlength=len(x))
print (x)


# Задача 5

# In[71]:



a=np.arange(16).reshape(4,4)
di= [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1, a.shape[1])]
b={j:di[j] for j in range(7)}
print (b)

