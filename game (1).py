
# coding: utf-8

# In[1]:

import turtle
import random
wn=turtle.Screen()
t1=turtle.Turtle()


# In[1]:

size=50
nMax=0
level="low"
wn.bgpic("Maze.gif")


# In[3]:

# def setPosition(pos):
#     t1.penup()
#     t1.setpos(pos)
#     t1.pendown()
#     t1.right(72)
#     t1.fd(20)
#     for k in range (0,4):
#         t1.right(144)
#         t1.fd(20)


# setPosition((좌표2개)) = 별그리는 함수, 위치에서 별을 하나 그린다.

# In[2]:

# def drawStars():
#     setPosition((200.00,200.00))
#     setPosition((-200.00,200.00))
#     setPosition((-200.00,-200.00))
#     setPosition((200.00,-200.00))
#     t1.penup()
#     t1.home()
#     t1.pendown()


# drawStars() = 게임을 위한 위치에 그림을 그리는 함수. 

# In[8]:

# drawStars()


# In[6]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[9]:

def MazeGame():
    print "go to t1 = 200.00,200.00"
    while (1):
        level=raw_input("Choose level : high, mid, low ")

        nMax = 0
        if (level=="high"):
            nMax=40
            break
        elif (level=="mid"):
            nMax=45
            break;
        elif(level=="low"):
            nMax=60
            break;
        else:
            print "잘못 입력하셨습니다."
    while (nMax!=0):
        curRegion=t1.pos()
        print curRegion, nMax
        if curRegion== (200.00,200.00):

            print "Let the game begin"
            player = raw_input("Enter your choice (rock/paper/scissors): ")
            player = player.lower()
            computer = random.randint(1,3)
            if (computer == 1):
                    computer = "rock"
            elif (computer == 2):
                    computer = "paper"
            elif (computer == 3):
                    computer = "scissors"
            else:
                print ("Error. Enter your choice from rock, paper, scissors.")

            if (player == computer):
                    print ("Draw!")
            elif (player == "rock"):
                if (computer == "paper"):
                        print ("You won.")
                        print("move count +5 ")
                        nMax=nMax+5
                if (computer == "scissors"):
                        print ("You lost.")
                        print("move count -5 ")
                        nMax=nMax-5
            elif (player == "paper"):
                if (computer == "rock"):
                        print ("You won.")
                        print("move count +5 ")
                        nMax=nMax+5
                if (computer == "scissors"):
                        print ("You lost.")
                        print("move count -5 ")
                        nMax=nMax-5
            elif (player == "scissors"):
                if (computer == "rock"):
                        print ("You lost.")
                        print("move count -5 ")
                        nMax=nMax-5
                if (computer == "paper"):
                        print ("You won.")
                        print("move count +5 ")
                        nMax=nMax+5
            t1.setpos(150,200)
	    print "go to t1 = -200.00,200.00 we must go to 200,-200"

        elif curRegion==(-200.00,200.00):
            print "Let the game begin, if you win, go to other site"
            x=int(raw_input("x size"))
            y=int(raw_input("y size"))
            print ("x^2 * y = ")
            xy=x*x*y
            Xy=raw_input("x^2 * y = ")
            Xy=int(Xy)
            if (xy==Xy):
                t1.penup()
                t1.setpos(-150,-150)
                t1.pendown()

        elif curRegion==(-200.00,-200.00):
            print "You touched traps. move count -2"
            nMax = nMax-2
            t1.setpos(-150,-150)

        elif curRegion==(200.00,-200.00):
            print "congraturation"
            break

        else:
            curser=raw_input()
            if (curser=="w"):
                t1.left(90)
                t1.fd(size)
            elif (curser=="d"):
                t1.fd(size)
            elif(curser=="s"):
                t1.right(90)
                t1.fd(size)
            elif(curser=="a"):
                t1.left(180)
                t1.fd(size)
            else:
                print("Error")
            t1.setheading(0)
            nMax=nMax-1


# In[ ]:

MazeGame()
## 게임 시작시 좌표 200,200으로 보내시면댑니다.

# # 좌표 이동 
# if (curser=="w"):
#     t1.left(90)
#     t1.fd(size)
# elif (curser=="d"):
#     t1.fd(size)
# elif(curser=="s"):
#     t1.right(90)
#     t1.fd(size)
# elif(curser=="a"):
#     t1.left(180)
#     t1.fd(size)
# else:
#     print("Error")
# t1.setheading(0)
# 

# In[ ]:

# def setPosition(pos):
#     t1.penup()
#     t1.setpos(pos)
#     t1.pendown()
#     t1.right(72)
#     t1.fd(20)
#     for k in range (0,4):
#         t1.right(144)
#         t1.fd(20) 

# def drawStars():
#     setPosition((200.00,200.00))
#     setPosition((-200.00,200.00))
#     setPosition((-200.00,-200.00))
#     setPosition((200.00,-200.00))
#     t1.penup()
#     t1.home()
#     t1.pendown()


# In[ ]:

# 	setPosition(pos)
# 	drawStars()


# In[ ]:



