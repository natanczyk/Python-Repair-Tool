def top_k(lst, k):
    # Fill in your code here
    sorted_list = custom_sort(lst[:])
    return sorted_list[:k]

def custom_sort(lst):
    result = []
    while lst:
        largest = lst[0]
        for elem in lst:
            if elem > largest:
                largest = elem
        lst.remove(largest)
        result.append(largest)
    return result