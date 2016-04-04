nMax=20
munja="*"
def starTriangle(munja) :
	for k in range(1, nMax):
		print " "*(nMax-k) + (munja* k) + ((k-1) * munja)

starTriangle("*")

def computeBMI(weight,height):
    bmi = float(weight/(height*height))
    if bmi  <= 18.5:
        print "low weight"
    elif bmi < 25.0:
        print "normal"
    elif bmi < 30.0:
        print"high weight"
    else:
        print "error"

    print bmi

computeBMI(50.0,1.5)

def lab5():
    weight = 50.0
    height = 1.5
    computeBMI(weight,height)
    
def main():
    lab5()
    starTriangle(munja)
    
if __name__=="__main__":
    main()
    
raw_input()
