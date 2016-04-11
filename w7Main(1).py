
# coding: utf-8

# In[7]:

def sum_list(LST=[]):
    LST=[]
    for j in range (0,1001):
        if j%4 ==0 and j%5!=0:
            LST.append(j)
    sum1 = 0 
    for i in range(0, len(LST)):
        sum1 = LST[i] + sum1
        
    return sum1
    return LST
    print sum1


# In[10]:

LST=list()

print sum_list(LST)


# In[11]:

raw_input()


# In[ ]:



