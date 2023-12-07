import heapq

def maximal_set(graph,thresholds):
    V, E = graph
    D=set()
    initial=len(V)
    print("Initial ",initial)
    
    dd = {v: len(neighbors) for v, neighbors in E.items()}
    gamma = {v: 0 for v in V}
    
    # handle one degree nodes
    degree_one_candidates = [v for v in V if dd[v] == 1]
    
    degree_heap=[(-dd[E[key][0]],E[key][0],key) for key in degree_one_candidates]
    heapq.heapify(degree_heap)
    while degree_heap:
        print("remaining nodes: ",len(V),"/",initial)
        max_degree,max_degree_neighbor,candidate=heapq.heappop(degree_heap)
        if max_degree_neighbor not in D:
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
        print("remaining nodes: ",len(V),"/",initial)
        
        u = max(V,key=dd.get)
        if u not in D:
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