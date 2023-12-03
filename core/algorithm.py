import numpy as np
import heapq

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
            print("IN PART TWO")
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
    

# Example usage:
graph = [
    {'A', 'B', 'C', 'D', 'E', 'F'},
    {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['B', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D', 'F'],
        'F': ['E'],
    }
]
# ans {B,E}

np.random.seed(42)

thresholds={node: 0.5 for node in graph[0]}


result = maximal_set(graph, thresholds)
print("Thresholds: ",thresholds)
print("Subset D:", result)


graph = [
    {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'},
    {
        '1':['8','13'],
        '2':['4'],
        '3':['5','7','8','11','15'],
        '4':['2','5','7'],
        '5':['4','3','6','7','8','15'],
        '6':['5','7'],
        '7':['6','5','4','3','8','11','12','13'],
        '8':['7','5','3','1','14','9','10'],
        '9':['8'],
        '10':['8','15'],
        '11':['7','3'],
        '12':['7'],
        '13':['7','1'],
        '14':['8'],
        '15':['10','5','3'],
    }
]

thresholds={node: 0.5 for node in graph[0]}
result = maximal_set(graph, thresholds)
print("Thresholds: ",thresholds)
print("Subset D:", result)

import pickle

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