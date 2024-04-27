from matplotlib import pyplot as plt

def plotBarDiagramm(reachabilityPlot):
    plt.bar(range(len(reachabilityPlot[0])), reachabilityPlot[1][:])
    plt.show()
    plt.clf()