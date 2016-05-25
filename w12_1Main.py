

import os
import time


fin = open('output.txt','r')
fout = open('outputUpper.txt', 'w')
stamp="ksm edited"
timeEdited=time.strftime('%Y-%m-%d %Y-%m-%d')
for line in fin:
    if line.find('line')!= -1:
        lines=line.replace('line','LINE')
        fout.write("[{0} {1}]{2}".format(stamp,timeEdited,lines))
    else :
        fout.write(line)

fin.close()
fout.close()

data=[1,2,3,4,5,6,7,8,9,10]
fout=open('outputNumber.txt','w')


for i in data:
    toPrint="{0}\t".format(i)
    if i%2==0:
        fout.write(toPrint+'\n')
    else :
        fout.write(toPrint)
    
fout.close()