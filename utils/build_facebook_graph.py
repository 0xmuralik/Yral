import sys
import pickle

def add_edge(u,v, graph):
    print("edge :", u, v)
    # Check if u is in the adjacency list; if not, add it as a key with an empty list as the value
    if u not in graph:
        graph[u] = []
    
    # Check if v is in the adjacency list; if not, add it as a key with an empty list as the value
    if v not in graph:
        graph[v] = []
    
    # Add v to the list of neighbors of u, and u to the list of neighbors of v
    graph[u].append(v)
    graph[v].append(u)
    print("added")

    # return graph

if len(sys.argv) != 2:
    print("Usage: python build_graph.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

# Initialize adjacency list for the graph
graph={}
lines_to_skip=2

try:
    with open(file_path, 'r') as file:
            
        for line in file:
            if lines_to_skip > 0:
                lines_to_skip -= 1
                continue
            
            u,v = line.split(" ")
            add_edge(u,v,graph)

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Serialize and save the graph to a file
with open('graph.pkl', 'wb') as file:
    pickle.dump(graph, file)
    
print("Graph has been serialized and saved to 'graph.pkl'.")