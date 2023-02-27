import random 

def pointGenerator(dimension, numOfPoints):
    pointList = []
    while numOfPoints > 0:
        itemPoint = []
        for i in range (dimension):
            itemPoint.append(random.randint(-100, 100))
        while (itemPoint in pointList):
            itemPoint = []
            for i in range (dimension):
                itemPoint.append(random.randint(-100, 100))
        pointList.append(itemPoint)
        numOfPoints = numOfPoints - 1
    return pointList; 
    
def stringDisplayGenerator(listPoint, numOfPoints, dimension):
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

def stringOutputGenerator(time, solution, dimension, distance, euclideanCount):
    text = ""
    text += "Time Taken: " + str(time) + "          Shortest Distance: " + str(distance)
    text += "      Euclidean Count: " + str(euclideanCount)
    text += "\nSolution (" + str(len(solution)) + "): "
    for i in range (len(solution) - 1):
        text += "{("
        for j in range (dimension - 1):
            text += str(solution[i][0][j])
            text += ", "
        text += str(solution[i][0][dimension-1])
        text += "), ("
        for j in range (dimension - 1):
            text += str(solution[i][1][j])
            text += ", "
        text += str(solution[i][1][dimension-1])
        text += ")}, "

    text += "{("
    for j in range (dimension - 1):
        text += str(solution[len(solution) - 1][0][j])
        text += ", "
    text += str(solution[len(solution) - 1][0][dimension-1])
    text += "), ("
    for j in range (dimension - 1):
        text += str(solution[len(solution) - 1][1][j])
        text += ", "
    text += str(solution[len(solution) - 1][1][dimension-1])
    text += ")}"

    return text