
# coding: utf-8

# In[8]:

nMax=20
munja="*"
def starTriangle(munja) :
    for k in range(1, nMax):
        print " "*(nMax-k) + (munja* k) + ((k-1) * munja)


# In[13]:

starTriangle("*")
starTriangle("@")


# In[ ]:



