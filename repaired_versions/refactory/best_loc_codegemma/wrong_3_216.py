def remove_extras(lst):
    i=0
    new = []
    while i<len(lst):    
        curr = lst[i]
        if curr not in new:
            new.append(curr)
        i +=1
    return new