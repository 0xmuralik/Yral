import numpy as np
import algorithm
import pickle
import sys

# optional: used random seed for testing purposes
# np.random.seed(42)

if len(sys.argv) != 3:
    print("Usage: python influence.py <graph_path> <mds_name>")
    sys.exit(1)

graph_path = sys.argv[1]
mds_path = sys.argv[2]+".pkl"

# Load the graph from a file
with open(graph_path, 'rb') as file:
    loaded_graph = pickle.load(file)
    graph = []
    graph.append(set(loaded_graph.keys()))
    graph.append(loaded_graph)
    thresholds={node: np.random.rand() for node in graph[0]}
    result = algorithm.minimal_dominating_set(graph, thresholds)
    print("Thresholds: ",thresholds)
    print("Subset D:", result)
    print("MDS size: ", len(result))
    with open(mds_path, 'wb') as file:
        pickle.dump(result, file)
        print("MDS saved to ",mds_path)