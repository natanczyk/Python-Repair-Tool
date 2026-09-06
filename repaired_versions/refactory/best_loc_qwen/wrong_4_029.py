def sort_age(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        lst1 = lst[:mid]
        lst2 = lst[mid:]
        
        lst1 = sort_age(lst1)
        lst2 = sort_age(lst2)
        
        return merge(lst1, lst2)

def merge(lst1, lst2):
    result = []
    while lst1 and lst2:
        if lst1[0][1] > lst2[0][1]:  # Descending order of age
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))
    result.extend(lst1)
    result.extend(lst2)
    return result