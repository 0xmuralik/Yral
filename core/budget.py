import pickle
import sys

if len(sys.argv) != 4:
    print("Usage: python budget.py <graph_path> <mds_path> <budget>")
    sys.exit(1)

graph_path = sys.argv[1]
mds_path = sys.argv[2]
budget = int(sys.argv[3])

graph = []
with open(graph_path, 'rb') as file:
    loaded_graph = pickle.load(file)
    graph.append(set(loaded_graph.keys()))
    graph.append(loaded_graph)

mds= {}  
with open(mds_path, 'rb') as file:
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

target=budget_cap(budget)

with open('target.pkl', 'wb') as file:
    pickle.dump(target, file)

print("Size of target set is: ", len(target))