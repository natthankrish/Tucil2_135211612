from PIL import Image
from matplotlib import pyplot as mplot

def getGraph(dimension, numOfPoints, listOfAllPoints, solution, maxAxisVal):
    mplot.close()
    
    if (dimension == 1):
        for i in range (numOfPoints):
            found = False
            for j in range (len(solution)):
                if listOfAllPoints[i] in solution[j]:
                    found = True
            if not found:
                mplot.plot(listOfAllPoints[i][0], 0, marker = "o", markersize = 4, markerfacecolor="green", markeredgecolor="green")
            else :
                mplot.plot(listOfAllPoints[i][0], 0, marker = "o", markersize = 4, markerfacecolor="red", markeredgecolor="red")

        for i in range (len(solution)): 
            mplot.plot([solution[i][0][0], solution[i][1][0]], [0,0], color="red")
    elif dimension == 2:
        mplot.xlim(maxAxisVal*-1,maxAxisVal)
        mplot.ylim(maxAxisVal*-1,maxAxisVal)

        mplot.grid()
        for i in range (numOfPoints):
            found = False
            for j in range (len(solution)):
                if listOfAllPoints[i] in solution[j]:
                    found = True
            if not found:
                mplot.plot(listOfAllPoints[i][0], listOfAllPoints[i][1], marker = "o", markersize = 4, markerfacecolor="green", markeredgecolor="green")
            else :
                mplot.plot(listOfAllPoints[i][0], listOfAllPoints[i][1], marker = "o", markersize = 4, markerfacecolor="red", markeredgecolor="red")

        for i in range (len(solution)):
            x = [solution[i][0][0], solution[i][1][0]]
            y = [solution[i][0][1], solution[i][1][1]]
            mplot.plot(x, y, color="red")
    elif dimension == 3:
        axis = mplot.axes(projection='3d')
        axis.set_xlim3d(maxAxisVal*-1,maxAxisVal)
        axis.set_ylim3d(maxAxisVal*-1,maxAxisVal)
        axis.set_zlim3d(maxAxisVal*-1,maxAxisVal)
        for i in range (numOfPoints):
            found = False
            for j in range (len(solution)):
                if listOfAllPoints[i] in solution[j]:
                    found = True
            if not found:
                axis.scatter3D(listOfAllPoints[i][0], listOfAllPoints[i][1], listOfAllPoints[i][2], color="green")
            else :
                axis.scatter3D(listOfAllPoints[i][0], listOfAllPoints[i][1], listOfAllPoints[i][2], color="red")
        
        for i in range (len(solution)):
            x = [solution[i][0][0], solution[i][1][0]]
            y = [solution[i][0][1], solution[i][1][1]]
            z = [solution[i][0][2], solution[i][1][2]]
            axis.plot3D(x, y, z, color="red")


    mplot.savefig("currentPlot.png")
