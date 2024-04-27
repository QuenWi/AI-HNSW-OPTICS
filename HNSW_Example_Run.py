import HNSW_OPTICS
from subscripts import datasets

dataset = datasets.dataset()
HNSW_OPTICS.hnsw_optics(dataset, 5, 28)