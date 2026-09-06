def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        group_u = group_by_node.setdefault(u, {u})
        group_v = group_by_node.setdefault(v, {v})
        
        if group_u != group_v:
            mst_edges.add(edge)
            # Merge the groups
            new_group = group_u.union(group_v)
            # Update all nodes in the merged group
            for node in new_group:
                group_by_node[node] = new_group

    return mst_edges