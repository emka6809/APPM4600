#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x = np.linspace(-5,10,100)


# In[3]:


y = x - 4*np.sin(2*x) - 3


# In[8]:


plt.plot(x,y)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.title('f(x) = x - 4sin(2x) - 3')
plt.show()


# In[ ]:




