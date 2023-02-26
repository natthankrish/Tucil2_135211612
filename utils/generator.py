import random 

def pointGenerator(dimension, numOfPoints):
    pointList = []
    while numOfPoints > 0:
        itemPoint = []
        for i in range (dimension):
            itemPoint.append(random.randint(0, 1000))
        while (itemPoint in pointList):
            itemPoint = []
            for i in range (dimension):
                itemPoint.append(random.randint(0, 1000))
        pointList.append(itemPoint)
        numOfPoints = numOfPoints - 1
    return pointList; 
    
def stringGenerator(listPoint, numOfPoints, dimension):
    listOfAllPoints = ""
    for i in range (numOfPoints - 1):
        listOfAllPoints = listOfAllPoints + str(i+1) + ". ("
        for j in range (dimension - 1):
            listOfAllPoints += str(listPoint[i][j])
            listOfAllPoints += ","
        listOfAllPoints += str(listPoint[i][dimension - 1])
        listOfAllPoints += ")\n"
    listOfAllPoints = listOfAllPoints + str(numOfPoints) + ". ("
    for j in range (dimension - 1):
        listOfAllPoints += str(listPoint[numOfPoints - 1][j])
        listOfAllPoints += ","
    listOfAllPoints += str(listPoint[numOfPoints - 1][dimension - 1])
    listOfAllPoints += ")"
    return listOfAllPoints