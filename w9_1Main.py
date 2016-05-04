import matplotlib
import matplotlib.pyplot as plt

def drawPlt(mydict):
    plt.bar(range(len(mydict)), mydict.values(),align='center')
    plt.xticks(range(len(mydict)),list(mydict.keys()))
    plt.show()

def countAlphaDigitLetters(word):
    word=word
    mydict=dict()
    count=0
    countDigit=0
    for c in word: 
        if c.isalpha():
            count = count + 1
            mydict['alpha']=count
        elif c.isdigit():
            countDigit = countDigit + 1
            mydict['digit']=countDigit
    return mydict

def home():

    myhome={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
    yourhome={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}

    print yourhome - myhome
    print myhome - yourhome
    print myhome | yourhome
    print myhome & yourhome

    d=dict()
    
    for i in myhome:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    for i in yourhome:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    print d 


def lab9_1():

    mydict=countAlphaDigitLetters("SANGMYUNG UNIVERSITY, 20, HONGIMUN 2-GIL, JONGNO-GU, SEOUL, REPUBLIC OF KOREA ")
    drawPlt(mydict)
    home()

def main():
    lab9_1()


if __name__ == "__main__":
    main()