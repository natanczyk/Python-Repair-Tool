def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.get):
        u, v = edge
        u_group = group_by_node.setdefault(u, {u})
        v_group = group_by_node.setdefault(v, {v})

        if u_group != v_group:
            mst_edges.add(edge)
            group_by_node[u].update(v_group)
            for node in v_group:
                group_by_node[node] = group_by_node[u]

    return mst_edges