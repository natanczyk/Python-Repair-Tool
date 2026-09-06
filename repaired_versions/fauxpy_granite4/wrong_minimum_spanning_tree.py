def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.get):
        u, v = edge
        if u not in group_by_node:
            group_by_node[u] = {u}
        if v not in group_by_node:
            group_by_node[v] = {v}
        
        if group_by_node[u] is not group_by_node[v]:
            mst_edges.add(edge)
            smaller, larger = (group_by_node[u], group_by_node[v]) if len(group_by_node[u]) < len(group_by_node[v]) else (group_by_node[v], group_by_node[u])
            larger.update(smaller)
            for node in smaller:
                group_by_node[node] = larger

    return mst_edges