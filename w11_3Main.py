import turtle
import math
wn = turtle.Screen()
t1= turtle.Turtle()
wn.bgpic("myMaze.gif")
p1=(100,200)
r=100

rect=[(100,100),(200, 200)]
line=[(50,100),(150,100)]
curpos=(100,0)

def drawLine():
    t1.penup()
    t1.goto(50,100)
    t1.setheading(0)
    t1.pendown()
    t1.fd(100)
    t1.penup()
    t1.goto(p1)
    t1.pendown()
    t1.circle(r)
    t1.penup()
    t1.goto(rect[0])
    t1.pendown()
    t1.goto(100,200)
    t1.goto(200,200)
    t1.goto(200,100)
    t1.goto(100,100)
    t1.penup()
    t1.home()
    t1.pendown()

def isinRectangle(curpos,rect):
    xs = rect[0][0]
    xe = rect[1][0]
    ys = rect[0][1]
    ye = rect[1][1]
    
    return xs <= curpos[0] <= xe and ys <= curpos[1] <= ye

    
def isOnLine(curpos,line):
    xs = line[0][0]
    xe = line[1][0]
    ys = line[0][1]
    ye = line[1][1]    
    if xs==xe:
        return xs-1 <= curpos[0] <=xe+1 and ys <= curpos[1] <= ys
        
    elif ys==ye:
        return xs <= curpos[0] <= xe and ys-1 <= curpos[1] <= ys+1
        
def isInCircle(curpos,p1,r):
    center = (p1[0],p1[1]+r)
    dist = math.sqrt(math.pow(center[0]-curpos[0],2)+math.pow(center[1]-curpos[1],2))
    if dist <= r :
        return True
    elif dist >= r :
        return False
    
def keyup():
    t1.fd(50)
    pt=t1.pos()
    if isOnLine(pt,line):
        t1.write(t1.pos())
    if isinRectangle(pt,rect):
        t1.write(t1.pos())
    if isInCircle(pt,p1,r):
        t1.write(t1.pos())

def keydown():
    t1.back(50)
    pt=t1.pos()

    if isOnLine(pt,line):
        t1.write(t1.pos())
    if isinRectangle(pt,rect):
        t1.write(t1.pos())
    if isInCircle(pt,p1,r):
        t1.write(t1.pos())
def keyleft():
    t1.left(45)
def keyright():
    t1.right(45)
def keybye():
	wn.bye() 

def mousegoto(x,y):
    t1.setpos(x,y)
    pt=t1.pos()
    if isOnLine(pt,line):
        t1.write(t1.pos())
    if isinRectangle(pt,rect):
        t1.write(t1.pos())
    if isInCircle(pt,p1,r):
        t1.write(t1.pos())

def addKeys():
	wn.onkey(keyup,"Up")
	wn.onkey(keydown, "Down")
	wn.onkey(keyleft, "Left")
	wn.onkey(keyright, "Right")
	wn.onkey(keybye, "q")
    
def addMouse():
	wn.onclick(mousegoto)
	
def isTouch():
	if mousegoto==(200,200):
		t1.home()
        
drawLine()
addKeys()
addMouse()
isTouch()
wn.listen()
turtle.mainloop()