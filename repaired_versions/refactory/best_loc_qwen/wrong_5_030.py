def top_k(lst, k):
    sort, output = [], []
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        lst.remove(largest)
        sort.append(largest)
    for j in sort[:k]:
        output.append(j)
    return output