#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Problem 4a


# In[1]:


import numpy as np


# In[2]:


import matplotlib.pyplot as plt


# In[4]:


t = np.arange(0,np.pi+ np.pi/40, np.pi/30)


# In[5]:


t


# In[6]:


y = np.array(np.cos(t))


# In[7]:


y


# In[27]:


n = 30
total_sum = 0
for i in range(0,n): 
    total_sum = total_sum + (t[i] * y[i])
print("The sum is", total_sum)


# In[28]:


## Problem 4b


# In[33]:


theta = np.linspace(0,2*np.pi,100)
R = 1.2
delta_r = 0.1
f = 15
p = 0


# In[37]:


x = R * (1+ delta_r*np.sin(f*theta +p))*np.cos(theta)
y = R * (1+ delta_r*np.sin(f*theta +p))*np.sin(theta)


# In[43]:


plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Single Wavy Circle')
plt.show()


# In[50]:


for i in range(0,11): 
    R2 = i
    delta_r2 = 0.05
    f2 = 2 + i
    p2 = np.random.uniform(0,2)
    x2 = R2 * (1+ delta_r2*np.sin(f2*theta +p2))*np.cos(theta)
    y2 = R2 * (1+ delta_r2*np.sin(f2*theta +p2))*np.sin(theta)
    plt.plot(x2,y2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('10 wavy circles')
plt.show()


# In[ ]:




