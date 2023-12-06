import numpy as np
import heapq
import pickle

def maximal_set(graph,thresholds):
    V, E = graph
    D=set()
    print("Initial ",len(V))
    
    dd = {v: len(neighbors) for v, neighbors in E.items()}
    gamma = {v: 0 for v in V}
    
    # handle one degree nodes
    degree_one_candidates = [v for v in V if dd[v] == 1]
    
    degree_heap=[(-dd[E[key][0]],E[key][0],key) for key in degree_one_candidates]
    heapq.heapify(degree_heap)
    while degree_heap:
        max_degree,max_degree_neighbor,candidate=heapq.heappop(degree_heap)
        if max_degree_neighbor not in D:
            print(max_degree_neighbor)
            D.add(max_degree_neighbor)
            if max_degree_neighbor in V:
                V.remove(max_degree_neighbor)
        
        for v in E[max_degree_neighbor]:
            if v in V:
                dd[v] -= 1
                gamma[v] += 1 / len(E[v])
                if gamma[v]>thresholds[v]:
                    V.remove(v)
        
        dd[max_degree_neighbor] = 0
        gamma[candidate] = 1
    
    while any(gamma[v] < thresholds[v] for v in V):
            print("remaining ",len(V))
            u = max(V,key=dd.get)
            if u not in D:
                print(u)
                D.add(u)
                if u in V:
                    V.remove(u)
            for v in E[u]:
                if v in V:
                    dd[v] -= 1
                    gamma[v] += 1 / len(E[v])
                    if gamma[v]>thresholds[v]:
                        V.remove(v)
                
    return D

np.random.seed(42)

# Load the graph from a file
with open('../utils/graph.pkl', 'rb') as file:
    loaded_graph = pickle.load(file)
    graph = []
    graph.append(set(loaded_graph.keys()))
    graph.append(loaded_graph)
    thresholds={node: np.random.rand() for node in graph[0]}
    result = maximal_set(graph, thresholds)
    print("Thresholds: ",thresholds)
    print("Subset D:", result)
    print("MDS size: ", len(result))
    with open('mds.pkl', 'wb') as file:
        pickle.dump(result, file)