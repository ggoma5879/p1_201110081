import turtle

class SquareTurtle(turtle.Turtle):
    def drawSquare(self):
        for i in range(0,4):
            self.fd(50)
            self.right(90)
    def drawSquare(self,size):
        for i in range(0,4):
            self.fd(size)
            self.right(90)
square1 = SquareTurtle()
square1.drawSquare(20)

class DogSound(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        print "my dog name is" , self.name
    def talk(self):
        print self.name,"mung mung"

class ShihTzuDog(object):
    def __init__(self, name):
        self.name = name
    def talk(self):
        print self.name,"si si"
        
class maltese(object):
    def __init__(self, name):
        self.name = name
    def talk(self):
        print self.name,"mal mal"

si = ShihTzuDog("sizu")
si.talk()

mal = maltese("malte")
mal.talk()

pu = DogSound("puppy")
pu.talk()