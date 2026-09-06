def shortest_paths(source, weight_by_edge):
    # Collect all nodes from edges and ensure source is included
    all_nodes = set()
    for u, v in weight_by_edge:
        all_nodes.add(u)
        all_nodes.add(v)
    all_nodes.add(source)
    
    weight_by_node = {node: float('inf') for node in all_nodes}
    weight_by_node[source] = 0

    # Bellman-Ford relaxation: V-1 iterations
    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    return weight_by_node