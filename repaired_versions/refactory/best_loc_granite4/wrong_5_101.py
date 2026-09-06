def top_k(lst, k):
    sorted_lst = sort(lst)
    return sorted_lst[:k]

def sort(lst):
    sorted_list = []
    while lst:
        largest = lst[0]
        for elem in lst:
            if elem > largest:
                largest = elem
        lst.remove(largest)
        sorted_list.append(largest)
    return sorted_list