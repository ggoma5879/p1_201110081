
import matplotlib
import matplotlib.pyplot as plt

def charCount(word):
    word=word
    mydict=dict()
    for c in word: 
        if c not in mydict:
            mydict[c]=1
        else:
            mydict[c]=mydict[c]+1
    return mydict


def drawPlt(mydict):
    plt.bar(range(len(mydict)), mydict.values(),align='center')
    plt.xticks(range(len(mydict)),list(mydict.keys()))
    plt.show()

def lab9():
    mydict=dict()
    mydict=charCount("my name is sung mo kim and i love jay park")
    drawPlt(mydict)

def main():
    lab9()

if __name__ == "__main__":
    main()