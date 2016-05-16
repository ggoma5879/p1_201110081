import turtle
wn = turtle.Screen()
t1= turtle.Turtle()
wn.bgpic("Maze.gif")

def drawLine():
	t1.penup()
	t1.goto(200,200)
	t1.setheading(0)
	t1.pendown()
	t1.fd(100)
	t1.penup()
	t1.home()
	t1.pendown()

def keyup():
    t1.fd(50)
def keydown():
    t1.back(50)
def keyleft():
    t1.left(45)
def keyright():
    t1.right(45)
def keybye():
	wn.bye() 

def mousegoto(x,y):
    t1.setpos(x,y)
    

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