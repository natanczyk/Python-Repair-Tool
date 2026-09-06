def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    lst_copy = list(lst)
    n = len(lst_copy) - k
    counter = 0
    # Remove the n smallest elements to leave only the top k
    while counter < n:
        lst_copy.remove(min(lst_copy))
        counter = counter + 1
    
    sort_list = []
    # Extract the remaining elements in descending order
    while lst_copy != []:
        val = max(lst_copy)
        sort_list.append(val)
        lst_copy.remove(val)
        
    return sort_list