def remove_extras(lst):
    listt = lst.copy()
    result = []
    seen = set()
    for element in listt:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result