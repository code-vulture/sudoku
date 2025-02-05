import random

r0 = []; r1 =  []; r2 = []; r3 = []; r4 = []; r5 = []; r6 = []; r7 = []; r8 = []

c0 = []; c1 =  []; c2 = []; c3 = []; c4 = []; c5 = []; c6 = []; c7 = []; c8 = []

b0 = []; b1 = []; b2 = []; b3 = []; b4= []; b5 = []; b6 = []; b7 = []; b8 = []


class sudoku:
    rows = [r0,r1,r2,r3,r4,r5,r6,r7,r8]
    columns = [c0,c1,c2,c3,c4,c5,c6,c7,c8]
    boxes = [b0,b1,b2,b3,b4,b5,b6,b7,b8]

def initialGen():
    numbers = (1,2,3,4,5,6,7,8,9)
    def genList(list):
        tempList = []
        num = random.random()*10;
        tempList.append(num)
        tempList.remove(num)
        return tempList
    # Generate row 0
    genList(r0)
    print(r0)

    def genListGiven(given, new):
        givenNums = [given]
        newList = new


    genListGiven(r0,c0)
    genListGiven(c0 + r0, b0)

    # Generate column 0

    # Generate box 0


initialGen()
