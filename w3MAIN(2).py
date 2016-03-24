
# coding: utf-8

# In[5]:

tmp = raw_input("What do you want to know F or C")


# In[6]:

if (tmp== 'F'):
    tmp1= float(raw_input("#C?"))
    tmp1 = tmp1 * (1.8) + 32
elif (tmp=='C'):
    tmp1= float(raw_input("#F?"))
    tmp1 = (tmp1-32)*5/9
else :
    print ("Error")
print "Temperature is ", tmp1, tmp


# In[ ]:

wn.exitonclick

