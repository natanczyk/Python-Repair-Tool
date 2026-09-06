def shortest_paths(source, weight_by_edge):
    # Get all unique nodes from the edges
    all_nodes = set()
    for u, v in weight_by_edge:
        all_nodes.add(u)
        all_nodes.add(v)
    
    # Initialize distances to all nodes as infinity
    weight_by_node = {
        node: float('inf') for node in all_nodes
    }
    weight_by_node[source] = 0

    # Relax edges repeatedly
    for i in range(len(all_nodes) - 1):
        for (u, v), weight in weight_by_edge.items():
            if weight_by_node[u] != float('inf'):
                weight_by_node[v] = min(
                    weight_by_node[v],
                    weight_by_node[u] + weight
                )

    return weight_by_node