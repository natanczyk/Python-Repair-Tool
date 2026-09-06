def top_k(lst, k):
    new_lst = []
    counter = 0
    while counter < k and lst:
        highest = max(lst)
        new_lst.append(highest)
        lst.remove(highest)
        counter += 1
        
    return new_lst