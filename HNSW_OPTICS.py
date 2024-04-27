from subscripts import HNSW_NN, OpticsCreateReachabilityPlot

def hnsw_optics(dataset, minPts, epsilonDistance):
    approximatedNN = HNSW_NN.getNearestNeighbors_Approximated(dataset, epsilonDistance*3)
    reachabilityPlot = OpticsCreateReachabilityPlot.createReachabilityplot(dataset, approximatedNN, minPts, epsilonDistance)
    print(reachabilityPlot)
    #ShowReachabilityPlot
    #Enter ReachabilityPlot Limit
    #Create Clusters
    #Show Clusters
    pass

