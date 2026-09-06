def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        if u not in group_by_node:
            group_by_node[u] = {u}
        if v not in group_by_node:
            group_by_node[v] = {v}

        if group_by_node[u] is not group_by_node[v]:
            mst_edges.add(edge)
            smaller_group = group_by_node[u] if len(group_by_node[u]) < len(group_by_node[v]) else group_by_node[v]
            larger_group = group_by_node[v] if smaller_group is group_by_node[u] else group_by_node[u]
            smaller_group.update(larger_group)
            for node in larger_group:
                group_by_node[node] = smaller_group

    return mst_edges