def top_k(lst, k):
    # Fill in your code here
    sorted_lst = sort(lst)
    return sorted_lst[:k]

def sort(lst):
    sorted_lst = []
    while lst:
        largest = lst[0]
        for elem in lst:
            if elem > largest:
                largest = elem
        lst.remove(largest)
        sorted_lst.append(largest)
    return sorted_lst