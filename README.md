# Yral - Social Influence Maximization using Minimal Dominating Sets

### Sample Datasets:
YouTube: https://www.kaggle.com/code/wolfram77/tree-graphs-snap-com-youtube/input?select=com-Youtube.mtx
Facebook: https://networkrepository.com/socfb-A-anon.php

## User guide

### Selecting datasets
Any text file which contains all the edges are supported, where 2 space seperated nodes in a new line means an edge between those 2 nodes.
Check out the sample youtube dataset mentioned above for reference.

### Build graph
To build the graph for your dataset use the command
```bash
python3 ./utils/build_graph.py <file_path> <edge_list_start_line> <graph_name>
```
`file_path`: Path to edge list file in your dataset
`edge_list_start_line`: Line number where the edge list starts
`graph_name`: File name to save the adjacency list representation of the graph.

Example:
```bash
python3 ./utils/build_graph.py ./datasets/youtube/com-Youtube.mtx 93 youtube-graph
```

### Derive Minimal Dominating Set
Use the graph generated above with `influence.py` program to generate MDS for your social network.
```bash
python3 ./core/influence.py <graph_path> <mds_name>
```
`graph_path`: Path to the graph(pickle file) generated earlier
`mds_name`: File name to save the resulting MDS.

Example:
```bash
python3 ./core/influence.py youtube-graph.pkl youtube-mds
```

It takes a couple of minutes to dervie the MDS for the youtube sample databse which has about 1.5 million nodes and 2.9 million edges.
The resulting MDS is about 390,000 nodes.

For the facebook dataset with 4 million nodes and 23.7 million edges, it takes 3 to 4 hours, to generate an MDS of about 670,000 nodes.


### Target nodes based on budget
To get a set of target nodes to infulence as many nodes as possible under a given budget, we select a subset of nodes from the MDS, where the cost of all the nodes in the subset is under a given budget.

```bash
python3 ./core/budget.py <graph_path> <mds_path> <budget> <target_set_name>
```
`graph_path`: Path to the graph(pickle file) generated earlier
`mds_path`: Path to the mds(pickle file) generated earlier
`budget`: Budget to influence the network
`target_set_name`: File name to save the resulting target set.

Example:
```bash
python3 ./core/budget.py youtube-graph.pkl youtube-mds.pkl 100000 youtube-target
```
