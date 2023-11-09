def influence_maximization(graph, threshold):
    V, E = graph  # Unpack the graph into vertices and edges
    D = set()     # Initialize D as an empty set

    # Initialize degree (dd) and influence (γ) values for each vertex
    dd = {v: len(neighbors) for v, neighbors in E.items()}
    gamma = {v: 0 for v in V}

    while any(gamma[v] < threshold for v in V - D):
        # Find vertices with degree 1 and γ < threshold
        degree_one_candidates = [v for v in V - D if dd[v] == 1 and gamma[v] < threshold]

        if degree_one_candidates:
            degree_one_neighbors = [E[v][0] for v in degree_one_candidates]
            s = max(degree_one_candidates, key=dd.get)  # Select vertex with max degree
            D.add(s)
            dd[s] = 0
            gamma[s] = 1
        else:
            u = max(V - D, key=dd.get)  # Select vertex with max dd value
            D.add(u)
            for v in E[u]:
                if v in V - D:
                    dd[v] -= 1
                    gamma[v] += 1 / len(E[v])

    return D


def maximal_set(graph,threshold):
    V, E = graph
    D=set()
    
    dd = {v: len(neighbors) for v, neighbors in E.items()}
    gamma = {v: 0 for v in V}
    
    while any(gamma[v] < threshold for v in V - D):
        
        degree_one_candidates = [v for v in V - D if dd[v] == 1 and gamma[v] < threshold]

        if degree_one_candidates:
            candidate=degree_one_candidates[0]
            max_degree_neighbor =  E[candidate][0]
            max_degree=0
            for v in degree_one_candidates:
                if(dd[E[v][0]]>max_degree):
                    max_degree=dd[E[v][0]]
                    max_degree_neighbor=E[v][0]
                    candidate=v
            
            print(max_degree_neighbor)
            D.add(max_degree_neighbor)
            for v in E[max_degree_neighbor]:
                if v in V - D:
                    dd[v] -= 1
                    gamma[v] += 1 / len(E[v])
            dd[max_degree_neighbor] = 0
            gamma[candidate] = 1
        else:
            u = max(V - D, key=dd.get)
            D.add(u)
            for v in E[u]:
                if v in V - D:
                    dd[v] -= 1
                    gamma[v] += 1 / len(E[v])
                
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

threshold = 0.5

result = maximal_set(graph, threshold)
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

result = maximal_set(graph, threshold)
print("Subset D:", result)
