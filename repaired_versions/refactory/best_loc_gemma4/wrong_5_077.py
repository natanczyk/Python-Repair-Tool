def top_k(lst, k):
    # Fill in your code here
 
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    result = []
    while temp_lst:
        maximum = temp_lst[0]  # arbitrary number in list 
        for x in temp_lst: 
            if x > maximum:
                maximum = x
        result.append(maximum)
        temp_lst.remove(maximum) 
    return result[:k]