def shortest_paths(source, weight_by_edge):
    weight_by_node = {v: float('inf') for v in set(u for u, _ in weight_by_edge.keys()) | set(v for _, v in weight_by_edge.keys())}
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            weight_by_node[v] = min(
                weight_by_node[v],
                weight_by_node[u] + weight
            )

    return weight_by_node