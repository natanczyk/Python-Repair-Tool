def sort_age(lst):
    if len(lst) <= 1:
        return lst
    else:
        used_lst = lst.copy()
        ages = tuple(i[1] for i in lst)
        max_age = max(ages)
        
        # Find the person with the maximum age
        for i in lst:
            if i[1] == max_age:
                new_lst = [i]
                used_lst.remove(i)
                break # Ensure we only take one person per recursive call
        
        return new_lst + sort_age(used_lst)