import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
pos=t1.pos
tracks=list()
for i in range(0,4):
	tracks.append(0)

def drawSquareAtSave(size,pos):
    t1.penup()
    t1.setpos(pos)
    t1.setheading(0)
    for i in range(0,4):
        t1.fd(size)
        t1.right(90)
        tracks[i]=t1.pos()
    return tracks

def drawSquareFrom():
    t1.penup()
    t1.setpos(tracks[3])
    t1.pendown()
    for i in range(0,4):
        t1.setpos(tracks[i])

def lab7():
    drawSquareAtSave(50,(50,50))
    drawSquareFrom()
	
def main():
	
	lab7()


if __name__=="__main__":
    main()
