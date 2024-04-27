import hnswlib

@staticmethod
def getNearestNeighbors_Approximated(dataset, k_Neighbors , hnsw_ef_Value = 10, hnsw_threads = 4, hnsw_ef_construction = 100 , hnsw_M = 16, hnsw_space = "l2"):
    rows = len(dataset)
    columns = len(dataset[0])
    if k_Neighbors > rows:
        k_Neighbors = rows
    p = hnswlib.Index(space = hnsw_space, dim = columns)
    p.init_index(max_elements = rows, ef_construction = hnsw_ef_construction, M = hnsw_M)
    p.set_ef(hnsw_ef_Value)
    p.set_num_threads(hnsw_threads)
    p.add_items(dataset)
    nearestNeighbors, distances = p.knn_query(dataset, k_Neighbors)
    del p
    return _HNSW_Approximated_NN(nearestNeighbors, distances)
    

class _HNSW_Approximated_NN:
    def __init__(self, nearestNeighbors, distances):
        self.nearestNeighbors = nearestNeighbors
        self.distances = distances