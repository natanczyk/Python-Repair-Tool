def shortest_paths(source, weight_by_edge):
    # Initialize distances to infinity for all nodes
    # We need to collect all nodes from the edges
    all_nodes = set()
    for u, v in weight_by_edge:
        all_nodes.add(u)
        all_nodes.add(v)
    
    weight_by_node = {node: float('inf') for node in all_nodes}
    weight_by_node[source] = 0

    # Bellman-Ford relaxation: repeat |V| - 1 times
    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    return weight_by_node