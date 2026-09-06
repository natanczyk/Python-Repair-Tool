def top_k(lst, k):
    if k < 0:
        return False
    if k == 0:
        return []
    if k > len(lst):
        return False
    
    # Create a copy of the list to avoid mutating the original input
    lst_copy = list(lst)
    
    if k == 1:
        return [max(lst_copy)]
    else:
        a = max(lst_copy)
        lst_copy.remove(a)
        # Return the current maximum combined with the result of the recursive call
        return [a] + top_k(lst_copy, k - 1)