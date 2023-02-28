def bruteForce(numOfPoints, listOfAllPoints):
    shortest = 9999
    solution = []
    euclideanCount = 0
    for i in range (numOfPoints - 1):
        for j in range (i+1, numOfPoints):
            distance = euclideanDistanceBrute(listOfAllPoints[i], listOfAllPoints[j])
            euclideanCount = euclideanCount + 1
            if (distance < shortest):
                shortest = distance
                solution = []
                solution.append([listOfAllPoints[i], listOfAllPoints[j]])
            elif (distance == shortest):
                solution.append([listOfAllPoints[i], listOfAllPoints[j]])
    return shortest, solution, euclideanCount

def euclideanDistanceBrute(pointA, pointB):
    sumSquare = 0
    for i in range (len(pointA)):
        sumSquare += (pointA[i]-pointB[i])**2
    return sumSquare ** 0.5