def top_k(lst, k):
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    counter = 0
    new_lst = []
    while counter < k:
        maxi = max(temp_lst)
        new_lst.append(maxi)
        temp_lst.remove(maxi)
        counter += 1
    return new_lst