def top_k(lst, k):
    # Sort the list in descending order
    lst.sort(reverse=True)
    # Return the top k elements
    return lst[:k]