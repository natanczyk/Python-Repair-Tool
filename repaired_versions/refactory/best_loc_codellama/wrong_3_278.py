def remove_extras(lst):
    if lst == []:
        return []
    else: 
        result = []
        for e in lst:
            if e not in result:
                result.append(e)
        return result