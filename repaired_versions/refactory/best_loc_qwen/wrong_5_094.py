def top_k(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):  # Adjust the range to avoid out-of-bound errors
            if lst[j] < lst[j + 1]:  # Change from > to < to sort in descending order
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Correct the swap logic
    
    return lst[:k]  # No need to reverse the list since we want the top k elements