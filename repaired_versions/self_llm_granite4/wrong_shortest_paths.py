def shortest_paths(source, weight_by_edge):
    # Collect all nodes that appear as either source or destination
    nodes = set()
    for u, v in weight_by_edge.keys():
        nodes.add(u)
        nodes.add(v)

    # Initialize distances
    weight_by_node = {node: float('inf') for node in nodes}
    weight_by_node[source] = 0

    # Relax edges |V| - 1 times
    for _ in range(len(nodes) - 1):
        for (u, v), weight in weight_by_edge.items():
            if weight_by_node[u] != float('inf') and weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    return weight_by_node