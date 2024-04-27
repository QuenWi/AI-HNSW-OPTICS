from subscripts import HNSW_NN, OpticsCreateReachabilityPlot, ShowBarDiagramm, CreateClustersFromReachablilityPlot, ShowResultCluster

def hnsw_optics(dataset, minPts, epsilonDistance):
    # Approximate NN
    approximatedNN = HNSW_NN.getNearestNeighbors_Approximated(dataset, epsilonDistance*3)
    # Create ReachablilityPlot
    reachabilityPlot = OpticsCreateReachabilityPlot.createReachabilityplot(dataset, approximatedNN, minPts, epsilonDistance)
    # Show ReachablilityPlot
    ShowBarDiagramm.plotBarDiagramm(reachabilityPlot)
    # Create Cluster
    cluster = CreateClustersFromReachablilityPlot.createClustersFromReachabilityPlot(reachabilityPlot)
    # Show Cluster
    ShowResultCluster.showPlot(dataset, cluster)
