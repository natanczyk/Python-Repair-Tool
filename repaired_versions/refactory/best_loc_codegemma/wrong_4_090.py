def sort_age(lst):
    holder=[]
    if lst==[]:
        return []
    for x in lst:
        if holder==[]:
            holder=x
        elif x[1]>holder[1]:
            holder=x
    return [holder]+sort_age(lst[:lst.index(holder)] + lst[lst.index(holder)+1:])