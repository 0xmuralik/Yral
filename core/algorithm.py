import heapq

# create minimal dominating set
def minimal_dominating_set(graph,thresholds):
    V, E = graph
    D=set()
    initial=len(V)
    print("Initial ",initial)
    
    # initialize deacresing degree and gamma(% of neighbors in MDS)
    dd = {v: len(neighbors) for v, neighbors in E.items()}
    gamma = {v: 0 for v in V}
    
    # get one degree nodes
    degree_one_candidates = [v for v in V if dd[v] == 1]
    
    # add neighbors of degree_one_candidates to max heap based on degree
    degree_heap=[(-dd[E[key][0]],E[key][0],key) for key in degree_one_candidates]
    heapq.heapify(degree_heap)
    
    # handle one degree nodes
    while degree_heap:
        print("remaining nodes: ",len(V),"/",initial)
        max_degree,max_degree_neighbor,candidate=heapq.heappop(degree_heap)
        if max_degree_neighbor not in D:
            # add max degree node to MDS
            D.add(max_degree_neighbor)
            if max_degree_neighbor in V:
                # remove MDS node from set of nodes V=(V-D)
                V.remove(max_degree_neighbor)
        
        # update dd and gamma for neighbors
        for v in E[max_degree_neighbor]:
            if v in V:
                dd[v] -= 1
                gamma[v] += 1 / len(E[v])
                
                # remove influenced nodes from V
                if gamma[v]>thresholds[v]:
                    V.remove(v)
        
        dd[max_degree_neighbor] = 0
        gamma[candidate] = 1
    
    # after handling one degree nodes
    while any(gamma[v] < thresholds[v] for v in V):
        print("remaining nodes: ",len(V),"/",initial)
        
        u = max(V,key=dd.get)
        if u not in D:
            # add max degree node to MDS and remove from V
            D.add(u)
            if u in V:
                V.remove(u)
        
        # update dd and gamma of neighbors
        for v in E[u]:
            if v in V:
                dd[v] -= 1
                gamma[v] += 1 / len(E[v])
                
                # remove influenced nodes from V
                if gamma[v]>thresholds[v]:
                    V.remove(v)
                
    return D