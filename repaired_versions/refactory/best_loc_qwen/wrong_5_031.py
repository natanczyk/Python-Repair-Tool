def top_k(lst, k):
    new_lst = []
    while lst and k > 0:
        largest = lst[0]
        for numbers in lst:
            if numbers > largest:
                largest = numbers
        index = lst.index(largest)
        new_lst.append(lst.pop(index))
        k -= 1
    return sorted(new_lst, reverse=True)