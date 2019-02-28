l = []
from random import randint

m = randint(1,100)

while(True):
    n = int(input("please enter your attempt number between 0 and 100 : "))

    l.append(n)

    if (l[-1]<0 or l[-1]>100): print("Out Of Bounds")

    elif (l[-1]==m ):
        print("congratulations you found the treasure")
        break

    elif len(l)==1 and  abs(l[-1]-m)>10 : print("Far Away")

    elif len(l)==1 and abs(l[-1]-m)<=10 : print("Close")

    elif abs(l[-1]-m)>abs(l[-2]-m) : print("Farther")

    elif abs(l[-1]-m)<abs(l[-2]-m) : print("Closer")

    elif  abs(l[-1]-m)==abs(l[-2]-m): print()



