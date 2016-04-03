
# coding: utf-8

# In[1]:

import random


# In[5]:

player = raw_input("Enter your choice (rock/paper/scissors): ")
player = player.lower()


# In[8]:

computer = random.randint(1,3)
if (computer == 1):
        computer = "rock"
elif (computer == 2):
        computer = "paper"
elif (computer == 3):
        computer = "scissors"
else:
    print ("Error. Enter your choice from rock, paper, scissors.")


# In[9]:

if (player == computer):
        print ("Draw!")
elif (player == "rock"):
    if (computer == "paper"):
            print ("You won.");
    if (computer == "scissors"):
            print ("You lost.");
elif (player == "paper"):
    if (computer == "rock"):
            print ("You won.");
    if (computer == "scissors"):
            print ("You lost.");
elif (player == "scissors"):
    if (computer == "rock"):
            print ("You lost.");
    if (computer == "paper"):
            print ("You won.");
             #restart
userInput = raw_input("Finish? Yes or No: ")
userInput = userInput.lower()
if (userInput == "yes"):
        play = False
        print ("See you again.")
else:
        play = True


# In[ ]:



