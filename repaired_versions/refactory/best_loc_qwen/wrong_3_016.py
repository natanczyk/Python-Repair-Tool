def remove_extras(lst):
    result = []
    counts = {}
    for i in lst:
        if i not in counts:
            counts[i] = 1
            result.append(i)
        else:
            counts[i] += 1
    
    return result