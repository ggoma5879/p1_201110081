listOfTuple=list()
distances=list()

kbg=tuple()
hj=tuple()
myj=tuple()
drm=tuple()
ghm=tuple()
ak=tuple()

kbg=(37.575729, 126.973519)
hj=(37.589056, 126.943558)
myj=(37.582184, 126.950336)
drm=(37.574577, 126.957784)
ghm=(37.571522, 126.976596)
ak=(37.576422, 126.985359)

listOfTuple=[kbg,hj,myj,drm,ghm,ak]

import math


for i in range(0,len(listOfTuple)):
    print (math.sqrt((listOfTuple[0][0]-listOfTuple[i][0])**2 + (listOfTuple[0][1]-listOfTuple[i][1])**2))

distances=[0.032791316685975284, 0.024064881341907405, 0.015777114089711337, 0.005212175937172186, 0.011860263445647059]


print min(distances), "is min"

 
