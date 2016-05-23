

import os
mydir = os.getcwd()


def readFile():

	mydir=os.getcwd()
	filename='python.txt'
	myfilename=os.path.join(mydir,filename)
	print myfilename


	try:
	    	myfile=open(myfilename,'r')

	except IOError as e :
    		print e

	contents=myfile.readlines()
	myfile.close()

	print contents

def writeFile():
 
	myfile=open('output.txt', 'w')
	line1='first line\n'	
	myfile.write(line1)
	line2='second line\n'
	myfile.write(line2)
	line3='third'
	myfile.write(line3)
	myfile.close()

	mydir=os.getcwd()
	filename='output.txt'
	myfilename=os.path.join(mydir,filename)
	print myfilename


	try:
	    	myfile=open(myfilename,'r')

	except IOError as e :
    		print e

	contents=myfile.readlines()
	myfile.close()

	for i in contents:
		if -1 != i.find("line"):
			print i.upper()

def lab12():
	readFile()
	writeFile()

def main():
	lab12()

main()