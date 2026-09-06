def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    result = []
    while temp_lst:
        biggest = temp_lst[0]
        for number in temp_lst:
            if number > biggest:
                biggest = number
        temp_lst.remove(biggest)
        result.append(biggest)
    return result[:k]