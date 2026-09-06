def top_k(lst, k):
    # Fill in your code here
    sorted_lst = sort(lst)
    return sorted_lst[:k]

def sort(lst):
    sorted_list = []
    lst_copy = lst[:]  # Make a copy to avoid modifying the original list
    while lst_copy:
        largest = lst_copy[0]
        for elem in lst_copy:
            if elem > largest:
                largest = elem
        lst_copy.remove(largest)
        sorted_list.append(largest)
    return sorted_list