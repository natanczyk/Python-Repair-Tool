from collections import defaultdict

def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    for i in range(n):
        for j in range(n):
            if (i, j) in length_by_edge:
                length_by_path[i, j] = length_by_edge[i, j]
            elif i == j:
                length_by_path[i, j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(
                    length_by_path[i, j],
                    length_by_path[i, k] + length_by_path[k, j]
                )

    return length_by_path