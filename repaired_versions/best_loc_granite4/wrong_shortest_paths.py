def shortest_paths(source, weight_by_edge):
    # Initialize distances from source to all nodes as infinite and source to itself as 0
    weight_by_node = {node: float('inf') for node in set().union(*weight_by_edge)}
    weight_by_node[source] = 0

    # Relax all edges |V| - 1 times
    for _ in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            if weight_by_node[u] != float('inf') and weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    return weight_by_node