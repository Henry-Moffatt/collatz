import math

bestCount=1
bestStartNum=1
bestX=[]
bestY=[]

lim = int(input("How many repetitons?"))
startNum= float(input("What is the start number"))

for i in range(lim):
    num=startNum
    repeat=True
    count = 1
    print(num)
    x=[]
    y=[]
    while repeat:
        count+=1
        x.append(count)
        if num % 2 == 0:
            num=num/2
            
        else:
            num= (3*num + 1)
            
        y.append(num)
        print(num)
        if num == 1:
            print(f"Collatz Conjecture has ended after {count} repetitions")
            if count > bestCount:
                bestCount = count
                bestStartNum = startNum
                bestX=x
                bestY=y
            startNum+=1
            repeat = False

print("Best number is:",bestStartNum, ", Taking", bestCount,"Repetitions")