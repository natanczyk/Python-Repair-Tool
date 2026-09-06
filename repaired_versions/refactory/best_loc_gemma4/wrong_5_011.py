def sort_age(lst):
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    new = []
    while temp_lst != []:
        big = temp_lst[0]
        for i in temp_lst:
            if i > big:
                big = i
        temp_lst.remove(big)
        new.append(big)
    return new

def top_k(lst, k):
    return sort_age(lst)[:k]