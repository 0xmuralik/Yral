import pickle

graph = []
with open('../utils/graph.pkl', 'rb') as file:
    loaded_graph = pickle.load(file)
    graph.append(set(loaded_graph.keys()))
    graph.append(loaded_graph)

mds= {}  
with open('mds.pkl', 'rb') as file:
    mds = pickle.load(file)

tuple_list = [(key, len(graph[1][key])) for key in mds]

sorted_tuple_list = sorted(tuple_list, key=lambda x: x[1])

sorted_mds = set(sorted_tuple_list)

def budget_cap(budget):
    target=set()
    for node,cost in sorted_mds:
        if budget>cost:
            budget-=cost
            target.add(node)
    
    return target

target=budget_cap(100000)

print(len(target))
print(len(mds))
print(len(graph[0]))