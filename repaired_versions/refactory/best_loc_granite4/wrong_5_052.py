def top_k(lst, k):
    # Implementing a simple selection sort to sort the list in descending order
    sorted_lst = lst[:]
    for i in range(len(sorted_lst)):
        max_idx = i
        for j in range(i + 1, len(sorted_lst)):
            if sorted_lst[j] > sorted_lst[max_idx]:
                max_idx = j
        sorted_lst[i], sorted_lst[max_idx] = sorted_lst[max_idx], sorted_lst[i]
    return sorted_lst[:k]