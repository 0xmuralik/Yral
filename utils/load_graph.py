import pickle

# Load the graph from a file
with open('graph.pkl', 'rb') as file:
    loaded_graph = pickle.load(file)

# Print the loaded graph
print("Graph loaded from file:")
print(loaded_graph)
