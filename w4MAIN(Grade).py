
# coding: utf-8

# In[6]:

import turtle

wn=turtle.Screen()


# In[7]:

def computerGrade(marks):
    if(90<=marks and marks<=100):
        grade='A'
    elif(80<=marks and marks<90):
        grade='B'
    elif(70<=marks and marks<80):
        grade='C'
    elif(60<=marks and marks<70):
        grade='D'
    else:
        grade='F'
    return grade


# In[21]:

def lab1():
    marks=raw_input("enter marks")
    marks=int(marks)
    mygrade=computerGrade(marks)
    print marks
    print mygrade


# In[22]:

def main():
    lab1()


# In[23]:

main()



# In[ ]:

wn.exitonclick()

