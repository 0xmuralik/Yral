import pickle
import sys

if len(sys.argv) != 5:
    print("Usage: python budget.py <graph_path> <mds_path> <budget> <target_set_name>")
    sys.exit(1)

graph_path = sys.argv[1]
mds_path = sys.argv[2]
budget = int(sys.argv[3])
target_file_path = sys.argv[4]+".pkl"

# load saved graph
graph = []
with open(graph_path, 'rb') as file:
    loaded_graph = pickle.load(file)
    graph.append(set(loaded_graph.keys()))
    graph.append(loaded_graph)

# load saved MDS
mds= {}  
with open(mds_path, 'rb') as file:
    mds = pickle.load(file)

# create (node,degree) pairs
tuple_list = [(key, len(graph[1][key])) for key in mds]

# sort based on degree
sorted_tuple_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)

sorted_mds = set(sorted_tuple_list)

# assume higher degree means higher cost (cost = degree)
def budget_cap(budget):
    target=set()
    for node,cost in sorted_mds:
        if budget>cost:
            budget-=cost
            # add highest degree node which is within budget
            target.add(node)
    
    return target

target=budget_cap(budget)

# save target nodes
with open(target_file_path, 'wb') as file:
    pickle.dump(target, file)
    print("Target set saved to file:",target_file_path)

print("Size of target set is: ", len(target))