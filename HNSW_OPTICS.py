from subscripts import HNSW_NN, OpticsCreateReachabilityPlot, ShowBarDiagramm, CreateClustersFromReachablilityPlot, ShowResultCluster

def hnsw_optics(dataset, minPts, epsilonDistance, Dataset2D = True):
    # Approximate NN
    approximatedNN = HNSW_NN.getNearestNeighbors_Approximated(dataset, minPts*3)
    # Create ReachablilityPlot
    reachabilityPlot = OpticsCreateReachabilityPlot.createReachabilityplot(dataset, approximatedNN, minPts, epsilonDistance)
    # Show ReachablilityPlot
    ShowBarDiagramm.plotBarDiagramm(reachabilityPlot)
    # Create Cluster
    cluster = CreateClustersFromReachablilityPlot.createClustersFromReachabilityPlot(reachabilityPlot)
    # Show Cluster
    if(Dataset2D):
        ShowResultCluster.showPlot(dataset, cluster)
    #return Cluster
    return cluster
