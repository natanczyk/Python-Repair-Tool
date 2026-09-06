def shortest_paths(source, weight_by_edge):
    # Initialize distances to infinity for all nodes in the graph
    # We need to collect all nodes from both keys (u, v) of weight_by_edge
    nodes = set()
    for u, v in weight_by_edge.keys():
        nodes.add(u)
        nodes.add(v)
    
    weight_by_node = {node: float('inf') for node in nodes}
    weight_by_node[source] = 0

    # Bellman-Ford algorithm: relax edges |V| - 1 times
    num_nodes = len(nodes)
    for i in range(num_nodes - 1):
        for (u, v), weight in weight_by_edge.items():
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    return weight_by_node