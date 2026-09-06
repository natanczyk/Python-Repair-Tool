def top_k(lst, k):
    # Fill in your code here
    sort = sorted(lst, reverse=True)
    return sort[:k]

def sort(lst):
    sort = []
    while lst:
        largest = lst[0]
        for elem in lst:
            if elem > largest:
                largest = elem
        lst.remove(largest)
        sort.append(largest)
    return sort