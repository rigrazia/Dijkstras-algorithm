
# Code is courtesty of ALEXEY KLOCHAY:
# https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html

import sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("\nWe found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))
    print("\n")
    
# nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
nodes = ["A", "B", "C", "D", "E", "F"]
 
init_graph = {}
for node in nodes:
    init_graph[node] = {}

'''    
init_graph["Reykjavik"]["Oslo"] = 5
init_graph["Reykjavik"]["London"] = 4
init_graph["Oslo"]["Berlin"] = 1
init_graph["Oslo"]["Moscow"] = 3
init_graph["Moscow"]["Belgrade"] = 5
init_graph["Moscow"]["Athens"] = 4
init_graph["Athens"]["Belgrade"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2   
'''

# Link States
init_graph["A"]["B"] = 1
init_graph["A"]["C"] = 5
init_graph["B"]["C"] = 2
init_graph["B"]["D"] = 1
init_graph["C"]["D"] = 2
init_graph["C"]["E"] = 2
init_graph["D"]["F"] = 2
init_graph["E"]["F"] = 5


print('''\n
Dikstra's Algorithm
-------------------

Python code courtesy of ALEXEY KLOCHAY:
https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html

My YouTube video on Dikstra's Alorithm which discusses the same topology used below:
https://youtu.be/3UQ7v3YdK2o
  
      
(A) --- 1 --- (B) --- 1 --- (D) --- 2 --- (F)
 |             |             |             |
 |             2    -- 2  ---              5
 |             |  /                        |
  5 --------- (C) ---------- 2 ---------- (E)
\n''')

# start_node_entered = "A"
# target_node_entered = "F"
start_node_entered = input("Enter starting node: ")
target_node_entered = input("Enter targe node: ")

start_node_entered = start_node_entered.upper()
target_node_entered = target_node_entered.upper()

graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start_node_entered)
print_result(previous_nodes, shortest_path, start_node=start_node_entered, target_node=target_node_entered)

