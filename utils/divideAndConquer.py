def shortestDistance(dimension, numOfPoints, listOfAllPoints):
    countEuclidean = 0
    max = -9999
    min = 9999
    for i in range (numOfPoints):
        if listOfAllPoints[i][dimension-1] > max:
            max = listOfAllPoints[i][dimension-1]
        if listOfAllPoints[i][dimension-1] < min:
            min = listOfAllPoints[i][dimension-1]
    divideAt = (max + min)/2
    left = []
    right = []
    for i in range (len(listOfAllPoints)):
        if listOfAllPoints[i][dimension-1] >= divideAt:
            right.append(listOfAllPoints[i])
        else:
            left.append(listOfAllPoints[i])
    shortest = 9999
    print(max, min, divideAt, left, right)
    solution = []

    if (dimension == 1):
        for i in range (len(right)):
            for j in range (i+1, len(right)):
                countEuclidean = countEuclidean + 1
                pointDistance = euclideanDistance(right[i], right[j])
                if (pointDistance < shortest):
                    solution.clear()
                    solution.append([right[i], right[j]])
                    shortest = pointDistance
                elif pointDistance == shortest:
                    solution.append([right[i], right[j]])

        for i in range (len(left)):
            for j in range (i+1, len(left)):
                countEuclidean = countEuclidean + 1
                pointDistance = euclideanDistance(left[i], left[j])
                if (pointDistance < shortest):
                    solution.clear()
                    solution.append([left[i], left[j]])
                    shortest = pointDistance
                elif pointDistance == shortest:
                    solution.append([left[i], left[j]])

    else:
        shortestRight = 9999
        shortestLeft = 9999
        countEuclideanRight = 0
        countEuclideanLeft = 0
        if (len(right) > 1):
            shortestRight, solutionRight, countEuclideanRight = shortestDistance(dimension-1, len(right), right)
        if (len(left) > 1):
            shortestLeft, solutionLeft, countEuclideanLeft = shortestDistance(dimension-1, len(left), left)
        if (shortestRight < shortestLeft):
            shortest = shortestRight
            solution = solutionRight
        else:
            shortest = shortestLeft
            solution = solutionLeft

        countEuclidean = countEuclideanLeft + countEuclideanRight

    print("count: ", countEuclidean)
    nearLine = []
    for i in range (len(listOfAllPoints)):
        if (listOfAllPoints[i][dimension-1] >= divideAt - shortest and listOfAllPoints[i][dimension-1] <= divideAt + shortest):
            nearLine.append(listOfAllPoints[i])
    print("nearline: ", nearLine)
    for i in range (len(nearLine)):
        for j in range (i+1, len(nearLine)):
            if ((nearLine[i] in right and nearLine[j] in left) or (nearLine[j] in right and nearLine[i] in left)):
                countEuclidean = countEuclidean + 1
                pointDistance = euclideanDistance(nearLine[i], nearLine[j])
                if (pointDistance < shortest):
                    solution.clear()
                    solution.append([nearLine[i], nearLine[j]])
                    shortest = pointDistance
                elif pointDistance == shortest:
                    if (not [nearLine[i], nearLine[j]] in solution):
                        solution.append([nearLine[i], nearLine[j]])

    print(shortest, solution, countEuclidean)
    print("-------")
    return (shortest, solution, countEuclidean)
        
    
        

            
def euclideanDistance(pointA, pointB):
    sumSquare = 0
    for i in range (len(pointA)):
        sumSquare += (pointA[i]-pointB[i])**2
    return sumSquare ** 0.5