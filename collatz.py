import numpy as np
from matplotlib import pyplot as plt

bestCount=1
bestStartNum=1
bestX=[]
bestY=[]

lim = int(input("How many repetitons? "))
startNum= float(input("What is the start number? "))

for i in range(lim):
    num=startNum
    repeat=True
    count = 1
    print(num)
    x=[]
    y=[]
    x=[count]
    y=[startNum]
    while repeat:
        
        count+=1
        
        
        if num % 2 == 0:
            num=num/2
            
        else:
            num= (3*num + 1)
            
        
        print(num)
        x.append(count)
        y.append(num)
        if num == 1:
            print(f"Collatz Conjecture has ended after {count} repetitions")
            if count > bestCount:
                bestCount = count
                bestStartNum = startNum
                
            
            xp=np.array(x)
            yp=np.array(y)
            print(yp)
            plt.plot(xp,yp)
            plt.title(f"Collatz Conjecture for {startNum}")
            plt.savefig(f"{startNum}.png")
            plt.show()
            startNum+=1
            repeat = False

print("Best number is:",bestStartNum, ", Taking", bestCount,"Repetitions")