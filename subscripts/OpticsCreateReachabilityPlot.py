import numpy as np

def createReachabilityplot(dataset, approximatedNN, minPts, epsilon):
    #Setup
    reachabilityPlot = [[], []]
    elementsInReachabilityPlot = [False for i in range(len(dataset))]
    #Fill Plot
    while True:
        #Get first object which is not in Reachability Plot
        index = 0
        while elementsInReachabilityPlot[index] == True:
            index +=1
            #All objects are in Reachability Plot
            if(index >= len(dataset)):
                return reachabilityPlot
        reachabilityList = [[], []]
        elementsInReachabilityPlot[index] = True
        #Add start  element
        reachabilityPlot[0].append(index)
        reachabilityPlot[1].append(eulerDistance(dataset[index], dataset[approximatedNN.nearestNeighbors[index][minPts]]))
        reachabilityList = fillList(dataset, approximatedNN, minPts, epsilon, index, reachabilityList, elementsInReachabilityPlot)
        if len(reachabilityList[0]) != 0:
            reachabilityList[0].pop(0)
            reachabilityList[1].pop(0)
        #Reachability List loop
        while len(reachabilityList[0]) != 0:
            #get shortest Connection
            shortestReachability = min(reachabilityList[1])
            indexOfObjectOfShortestConnection = reachabilityList[1].index(shortestReachability)
            objectOfShortestConnection = reachabilityList[0][indexOfObjectOfShortestConnection]
            #Save Result in reachabilityplot
            reachabilityPlot[0].append(objectOfShortestConnection)
            reachabilityPlot[1].append(shortestReachability)
            if len(reachabilityList[0]) == 0:
                break
            #Update Lists
            elementsInReachabilityPlot[objectOfShortestConnection] = True
            reachabilityList[0].pop(indexOfObjectOfShortestConnection)
            reachabilityList[1].pop(indexOfObjectOfShortestConnection)
            reachabilityList = fillList(dataset, approximatedNN, minPts, epsilon, objectOfShortestConnection, reachabilityList, elementsInReachabilityPlot)

def fillList(dataset, approximatedNN, minPts, epsilon, index, reachabilityList, elementsInReachabilityPlot):
    #Core or Noise
    if epsilon < eulerDistance(dataset[index], dataset[approximatedNN.nearestNeighbors[index][minPts]]):
        #Object is Noise
        return reachabilityList
    else:
        #Object is Core
        minPtsDistance = eulerDistance(dataset[index], dataset[approximatedNN.nearestNeighbors[index][minPts]])
        for i in range(minPts):
            reachabilityList = reachabilityListUpdate(approximatedNN.nearestNeighbors[index][i], minPtsDistance, reachabilityList, elementsInReachabilityPlot)
        counter = minPts
        while counter < minPts*3 and epsilon > eulerDistance(dataset[index], dataset[approximatedNN.nearestNeighbors[index][counter]]):
            reachabilityList = reachabilityListUpdate(approximatedNN.nearestNeighbors[index][counter], eulerDistance(dataset[index], dataset[approximatedNN.nearestNeighbors[index][counter]]), reachabilityList, elementsInReachabilityPlot)
            counter += 1
        return reachabilityList
    
def reachabilityListUpdate(object, distance, reachabilityList, elementsInReachabilityPlot):
    if elementsInReachabilityPlot[object] == False:
        if object in reachabilityList[0]:
            if distance < reachabilityList[0].index(object):
                reachabilityList[1][reachabilityList[0].index(object)] = distance
        else:
            reachabilityList[0].append(object)
            reachabilityList[1].append(distance)
    return reachabilityList

def eulerDistance(object1, object2):
    return np.linalg.norm(object1-object2)