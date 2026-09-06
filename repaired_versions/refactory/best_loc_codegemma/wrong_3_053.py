def remove_extras(lst):
    seen = set()
    new_lst = []
    for num in lst:
        if num not in seen:
            new_lst.append(num)
            seen.add(num)
    return new_lst