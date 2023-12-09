import sys
import pickle

def add_edge(u,v, graph):
    
    # Check if u is in the adjacency list; if not, add it as a key with an empty list as the value
    if u not in graph:
        graph[u] = []
    
    # Check if v is in the adjacency list; if not, add it as a key with an empty list as the value
    if v not in graph:
        graph[v] = []
    
    # Add v to the list of neighbors of u, and u to the list of neighbors of v
    graph[u].append(v)
    graph[v].append(u)
    print("added edge :", u, v)


if len(sys.argv) != 4:
    print("Usage: python build_graph.py <file_path> <edge_list_start_line> <graph_name>")
    sys.exit(1)

file_path = sys.argv[1]
lines_to_skip=int(sys.argv[2])-1
graph_name = sys.argv[3]

# Initialize adjacency list for the graph
graph={}

try:
    with open(file_path, 'r') as file:
        
        # Skip line before edge list
        for line in file:
            if lines_to_skip > 0:
                lines_to_skip -= 1
                continue
            
            # add edges to graph
            u,v = line.split(" ")
            add_edge(u,v,graph)

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Serialize and save the graph to a file
with open(graph_name+'.pkl', 'wb') as file:
    pickle.dump(graph, file)
    print("Graph has been serialized and saved to",graph_name+".pkl")