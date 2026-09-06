def top_k(lst, k):
    # Fill in your code here
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    sort = []
    while temp_lst:
        largest = temp_lst[0]
        for i in range(len(temp_lst)):
            if temp_lst[i] > largest:
                largest = temp_lst[i]
        sort.append(largest)
        temp_lst.remove(largest)
    return sort[:k]