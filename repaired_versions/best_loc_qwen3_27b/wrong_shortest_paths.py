def shortest_paths(source, weight_by_edge):
    # Collect all nodes from edges and ensure source is included
    nodes = set()
    for u, v in weight_by_edge:
        nodes.add(u)
        nodes.add(v)
    nodes.add(source)
    
    weight_by_node = {node: float('inf') for node in nodes}
    weight_by_node[source] = 0

    # Bellman-Ford relaxation: repeat |V| - 1 times
    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    return weight_by_node