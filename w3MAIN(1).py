
# coding: utf-8

# In[3]:

import turtle
wn = turtle.Screen()
t1= turtle.Turtle()


# In[6]:

sel = raw_input("Triangle or Square: ")


# In[7]:

if(sel=='T'):
    print "you entered T"
    size= 100
    angle = 120
    sides =3
    for i in range(sides):
        t1.fd(size)
        t1.right(angle)
else :
    print "you entered S"
    size = 100
    angle = 90
    sides = 4
    for i in range(sides):
        t1.fd(size)
        t1.right(angle)


# In[ ]:

wn.exitonclick()


# In[ ]:



