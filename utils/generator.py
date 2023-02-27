import random 

def pointGenerator(dimension, numOfPoints, maxAxisVal):
    pointList = []
    while numOfPoints > 0:
        itemPoint = []
        for i in range (dimension):
            itemPoint.append(random.randint(maxAxisVal*-1, maxAxisVal))
        while (itemPoint in pointList):
            itemPoint = []
            for i in range (dimension):
                itemPoint.append(random.randint(maxAxisVal*-1, maxAxisVal))
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
    text += "      Euclidean Count: " + str(euclideanCount) + "\nSolution (" + str(len(solution)) + "): "
    
    strsol = ""
    for i in range (len(solution) - 1):
        strsol += "{("
        for j in range (dimension - 1):
            strsol += str(solution[i][0][j])
            strsol += ", "
        strsol += str(solution[i][0][dimension-1])
        strsol += "), ("
        for j in range (dimension - 1):
            strsol += str(solution[i][1][j])
            strsol += ", "
        strsol += str(solution[i][1][dimension-1])
        strsol += ")}, "

    strsol += "{("
    for j in range (dimension - 1):
        strsol += str(solution[len(solution) - 1][0][j])
        strsol += ", "
    strsol += str(solution[len(solution) - 1][0][dimension-1])
    strsol += "), ("
    for j in range (dimension - 1):
        strsol += str(solution[len(solution) - 1][1][j])
        strsol += ", "
    strsol += str(solution[len(solution) - 1][1][dimension-1])
    strsol += ")}"

    if len(strsol) < 100:
        text += strsol
    else:
        text += "Check Terminal"
    return text