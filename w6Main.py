"""
@author KSM
@since 160406
"""
def multiple3and5():
    print "sum of multiple 3 and 5"
    startNumber=int(raw_input("set a start number\n"))
    number=int(raw_input("set a objective number\n"))
    sum=0
    for i in range(startNumber,number+1):
        if (i%3==0):
            sum=i+sum
        elif (i%5==0):
            sum=i+sum
    print "sum :",sum

def findQYear():
    qYear=int(raw_input("leap year = what year are you wondering?"))
    if ((qYear % 4 == 0 and qYear% 100 != 0) or qYear % 400 == 0):
        print qYear,"is leap YEAR."
    else :
        print "No,",qYear,"is not leap year"

def upAndDown():
    print "High low game, first user enter the hidden number and the guess user turn"
    nMax=1000
    i=1
    obNumber = 0
    count=0
    obNumber =int(raw_input("hidden number"))
    

    while( i!=0):
        number=int(raw_input("input number"))
        if number == obNumber:
            print "CORRECT"
            break
        elif number <= obNumber:
            print "up"
        elif number >= obNumber :
            print "down"   
        else :
            print "Error, plz enter numbers"
        count= count + 1
    print "Correct, you guessed just" ,count+1 

def lab6():
    multiple3and5()
    
def lab6_1():
    findQYear()

def lab6_2():
    upAndDown()

def main():
    lab6()
    lab6_1()
    lab6_2()

if __name__=="__main__":
    main()

