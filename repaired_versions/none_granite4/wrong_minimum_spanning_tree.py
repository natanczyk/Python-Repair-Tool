def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    
    def find(node):
        if group_by_node[node] != node:
            group_by_node[node] = find(group_by_node[node])
        return group_by_node[node]
    
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            group_by_node[root2] = root1
    
    mst_edges = set()
    
    for u, v in sorted(weight_by_edge, key=weight_by_edge.get):
        if u not in group_by_node:
            group_by_node[u] = u
        if v not in group_by_node:
            group_by_node[v] = v
        
        if find(u) != find(v):
            mst_edges.add((u, v))
            union(u, v)
    
    return mst_edges