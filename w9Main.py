
import matplotlib
import matplotlib.pyplot as plt

def listOfThings():
    statics=[[74425, 76326],[61164, 61636],[109688, 115744],[144796, 146776],[174996, 181676],[177841, 177434],[204630, 205980],[223373, 232245]
         ,[161055, 166130],[171576, 176735],[279169, 293772],[239450, 251066],[148690, 156510],[182977, 196992],[237792, 242641]
         ,[283869, 296762],[209344, 210282],[118965, 114441],[186503, 186856],[195734, 203014],[254381, 249472],[212401, 229111],[271654, 295354]
        ,[319197, 335045],[229829, 231671]]
    
    manSum=0
    womanSum=0
    gu_sumOfStatics=[]
    AveOfStatics=[]
    gender_sumOfStatics=[]
    for i in statics:
        gu_sumOfStatics.append(i[0]+i[1])
    for i in statics:
        manSum=i[0]+manSum
        womanSum=i[1]+womanSum
    
    gender_sumOfStatics.append(manSum)
    gender_sumOfStatics.append(womanSum)

    AveOfStatics.append(manSum/len(statics))
    AveOfStatics.append(womanSum/len(statics))
        
    return gu_sumOfStatics, AveOfStatics, gender_sumOfStatics




def lab10_1():
    listOfThings()

def main():
    lab10_1()

if __name__ == "__main__":
    main()