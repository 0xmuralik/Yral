import pickle
import algorithm


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

with open('../utils/graph-demo1.pkl', 'wb') as file:
    pickle.dump(graph[1], file)

# ans {B,E}

# didnt use random thresholds for demos for better understanding
thresholds={node: 0.5 for node in graph[0]}


result = algorithm.maximal_set(graph, thresholds)
print("Thresholds: ",thresholds)
print("Subset D:", result)

with open('mds-demo1.pkl', 'wb') as file:
    pickle.dump(result, file)


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

with open('../utils/graph-demo2.pkl', 'wb') as file:
    pickle.dump(graph[1], file)

# didnt use random thresholds for demos for better understanding
thresholds={node: 0.5 for node in graph[0]}
result = algorithm.minimal_dominating_set(graph, thresholds)
print("Thresholds: ",thresholds)
print("Subset D:", result)
with open('mds-demo2.pkl', 'wb') as file:
    pickle.dump(result, file)
