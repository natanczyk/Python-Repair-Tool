def sort_age(lst):
    holder=[]
    if lst==[]:
        return []
    for x in lst:
        if holder==[]:
            holder=x
        elif x[1]>holder[1]:
            holder=x
    # Create a new list without the holder element instead of using remove() which modifies in-place and returns None
    new_lst = [x for x in lst if x != holder]
    return [holder]+sort_age(new_lst)