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


def lab6():
    multiple3and5()
    
def lab6_1():
    findQYear()

def main():
    lab6()
    lab6_1()

if __name__=="__main__":
    main()

