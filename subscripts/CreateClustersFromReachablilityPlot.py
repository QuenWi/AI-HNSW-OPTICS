

def createClustersFromReachabilityPlot(reachabilityPlot):
    cluster = [[]]
    print("What is the limit reachability?:")
    limit = float(input())
    counter = 0
    while counter < len(reachabilityPlot[0]):
        if limit <= reachabilityPlot[1][counter]:
            cluster.append([])
        cluster[len(cluster)-1].append(reachabilityPlot[0][counter])
        counter += 1
    return cluster