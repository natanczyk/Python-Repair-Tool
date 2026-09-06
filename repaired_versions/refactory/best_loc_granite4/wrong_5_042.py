def top_k(lst, k):
    # top k in descending order
    result = []
    while k > 0 and lst:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        result.append(largest)
        k -= 1
    return result