import turtle
import random
import time
import math
import os
wn = turtle.Screen()
t1= turtle.Turtle()
rect=[(180,180),(220, 220)]
rect1=[(-220,180),(-180, 220)]
rect2=[(-220, -220),(-180,-180)]
rect3=[(180,-220),(220, -180)]
pt=t1.pos()

 
f = turtle.Turtle()
e1 = turtle.Turtle()
ef = turtle.Turtle()
mh1 = turtle.Turtle()
mh2 = turtle.Turtle()
mh3 = turtle.Turtle()
mh4 = turtle.Turtle()
mh5 = turtle.Turtle()
wn.screensize(50,50)
wn.bgpic("back.gif")
wn.register_shape("front.gif")
wn.register_shape("fire.gif")
wn.register_shape("monster.gif")
wn.register_shape("HP.gif")
wn.register_shape('flower.gif')
wn.register_shape('front2.gif')
wn.register_shape('e2.gif')
wn.register_shape('e1.gif')
mh1.shape('HP.gif')
mh2.shape('HP.gif')
mh3.shape('HP.gif')
mh4.shape('HP.gif')
mh5.shape('HP.gif')
t1.shape('front.gif')


def smallCount():
    mh1.speed(0)
    mh2.speed(0)
    mh3.speed(0)
    mh4.speed(0)
    mh5.speed(0)
    mh1.penup()
    mh1.goto(362,-55)
    mh1.st()
    mh2.penup()
    mh2.goto(387,-55)
    mh2.st()
    mh3.penup()
    mh3.goto(412,-55)
    mh3.st()    
    mh4.penup()
    mh4.goto(437,-55)
    mh4.st()
    mh5.penup()
    mh5.goto(462,-55)
    mh5.st()



def hpdown():
    
    if mh2.isvisible()==False:
        mh1.ht()
        gameover()
    elif mh3.isvisible()==False:
        mh2.ht()
    elif mh4.isvisible()==False:
        mh3.ht()
    elif mh5.isvisible()==False:
        mh4.ht()
    else:
        mh5.ht()
def hpup():
    if mh5.isvisible()==False:
        mh5.st()
    elif mh4.isvisible()==False:
        mh4.st()
    elif mh3.isvisible()==False:
        mh3.st()
    elif mh2.isvisible()==False:
        mh2.st()


def Stamp():
    mydir=os.getcwd()
    filename1='output1.txt'
    filename2='output2.txt'
    myfilename1=os.path.join(mydir,filename1)
    myfilename2=os.path.join(mydir,filename2)
    stamp = raw_input("user name : ")
    my=open(myfilename1,'w')
    my.write("l")
    my.close()
    try:
        fin = open(myfilename1,'r')
        fout = open(myfilename2, 'w')
        timeEdited=time.strftime('%Y-%m-%d %Hh %Mm %Ss')

        for line in fin:
            fout.write("[{0}] - {1}]{2}".format(stamp,timeEdited,line)+'\n')
        fin.close()
        fout.close()

        fout = open(myfilename2,'r')
        fin = open(myfilename1,'w')
        for line in fout:
            fin.write(line)
        fin.close()
        fout.close()
    except Exception as e:
        print e

def keyup():
    t1.fd(50)
    pt=t1.pos()
    if isinRectangle(pt,rect):
        DiceGame()
    if isinRectangle(pt,rect1):
        TrainOrder()
    if isinRectangle(pt,rect2):
        Trap()
    if isinRectangle(pt,rect3):
        Finish()
def keydown():
    t1.back(50)
    pt=t1.pos()
    if isinRectangle(pt,rect):
        DiceGame()
    if isinRectangle(pt,rect1):
        TrainOrder()
    if isinRectangle(pt,rect2):
        Trap()
    if isinRectangle(pt,rect3):
        Finish()
def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keybye():
	wn.bye() 

def mousegoto(x,y):

    if isinRectangle(pt,rect):
        DiceGame()
    if isinRectangle(pt,rect1):
        trainOrder()
    if isinRectangle(pt,rect2):
        Trap()
    if isinRectangle(pt,rect1):
        Finish()
    t1.setpos(x,y)
    
def addKeys():
	wn.onkey(keyup,"Up")
	wn.onkey(keydown, "Down")
	wn.onkey(keyleft, "Left")
	wn.onkey(keyright, "Right")
	wn.onkey(keybye, "q")
def addMouse():
	wn.onclick(mousegoto)

def isinRectangle(pt,rect): 
    xs = rect[0][0]
    xe = rect[1][0]
    ys = rect[0][1]
    ye = rect[1][1]
    return xs <= pt[0] <= xe and ys <= pt[1] <= ye

def setPosition(pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    t1.right(72)
    t1.fd(20)
    for k in range (0,4):
        t1.right(144)
        t1.fd(20)

def drawStars():
    setPosition((200.00,200.00))
    setPosition((-200.00,200.00))
    setPosition((-200.00,-200.00))
    setPosition((200.00,-200.00))
    t1.penup()
    t1.home()
    t1.pendown()

def DiceGame():
    curRegion=t1.pos()
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
                hpup()
                print ("You won.")
                print("hp : +1 ")
                
        if (computer == "scissors"):
                hpdown()
                print ("You lost.")
                print("hp : -1 ")
                
    elif (player == "paper"):
        if (computer == "rock"):
                hpup()
                print ("You won.")
                print("hp : +1 ")                
        if (computer == "scissors"):
                print ("You lost.")
                hpdown()
                print("hp : -1 ")
                
    elif (player == "scissors"):
        if (computer == "rock"):
                print ("You lost.")
                hpdown()
                print("hp : -1 ")
               
        if (computer == "paper"):

            	hpup()
                print ("You won.")
                print("hp : +1 ")                
 
    t1.goto(150,150)


def Trap():
    print "You touched traps. hp: -1"
    hpdown()
    t1.setpos(-150,-150)

def Finish():
    print "congraturation"
    turtle.clearscreen()
    wn = turtle.Screen()
    wn.bgpic('clear.gif')

def TrainOrder():
    cycle = 1
    user = list()
    row="A-B-C-D-E-F"
    for i in range(0,cycle):
        user.append(raw_input("Order the station Ex) A-B-C-D-E-F"))
    mylist = list()
    for q in range(0,cycle):
        aq=list()
        for station in user[q].split('-'):
            aq.append(station)
    trainOrder= list()
    for order in row.split('-'):
        trainOrder.append(order)
    myorder=list()
    for order in row.split('-'):
        myorder.append(order)
    
    for i in range(0,len(aq)): 
        if aq[i]=="A":
            k=0
            while(1):
                if myorder[len(myorder)-1-k] == "0":
                    if(len(myorder)-1-k)=="0":
                        print "No more"
                        break;
                    k=k+1
                else : 
                    if k==0:
                        myorder.append("A")

                    else:
                        myorder.append("0")
                        for j in range(0,len(myorder)):
                            myorder[len(myorder)-1-j]=myorder[len(myorder)-2-j]
                        myorder[0]="B"
                        print myorder

                    break;
        elif aq[i]=="B":
            k=0
            while(1):
                if myorder[len(myorder)-1-k] == "0":
                    if(len(myorder)-1-k)=="0":
                        print "No more"
                        break;
                    k=k+1
                else : 
                    if k==0:
                        myorder.append("A")
                    else:
                        myorder[len(myorder)-k]="A"
                    print myorder    
                    break;
        elif aq[i]=="C":
            k=0
            for j in range(2,len(myorder)):
                myorder[j-1]=myorder[j]
            myorder[len(myorder)-1]="0"
            print myorder
        elif aq[i]=="D":
            k=0
            for j in range(0,len(myorder)-1):
                myorder[j]=myorder[j+1]
            myorder[len(myorder)-1]="0"
            print myorder
        elif aq[i]=="E":
            trainOrder[0]=myorder[0]
            k=0
            while(1):
                if myorder[len(myorder)-1-k] == "0":
                    k=k+1
                    if(len(myorder)-1-k)=="0":
                        print "No more"
                        break;
                else : 
                    trainOrder[1]=myorder[len(myorder)-1-k]
                    myorder[len(myorder)-1-k]= trainOrder[0]
                    break;
            myorder[0]= trainOrder[1]
            print myorder
        elif aq[i]=="F":
            k=0
            while(1):
                if myorder[len(myorder)-1-k] == "0":
                    k=k+1
                    if(len(myorder)-1-k)=="0":
                        print "No more"
                        break;
                else : 
                    trainOrder[0]=myorder[len(myorder)-2-k]
                    trainOrder[1]=myorder[len(myorder)-1-k]
                    myorder[len(myorder)-2-k]=trainOrder[1]
                    myorder[len(myorder)-1-k]=trainOrder[0]
                    break;
            print myorder
    
    print "CASE#",q,myorder
    for i in range (0,len(myorder)):
        if myorder[i]== '0':
            hpdown()   

def gameover():
    turtle.clearscreen()
    wn = turtle.Screen()
    wn.bgpic('gameover.gif')

Stamp()
addKeys()
addMouse()
drawStars()
smallCount()

wn.listen()
turtle.mainloop()