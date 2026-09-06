def top_k(lst, k):
    i=0
    while i+1<len(lst):
        if lst[i]<lst[i+1]:
            lst.insert(i, lst.pop(i+1))
            i=0
        else:
            i+=1
    return lst[:k]