def sort_age(lst):
    new = []
    while lst:
        large = lst[0][1]
        name = lst[0][0]
        for ele in lst:
            if ele[1] > large:
                large = ele[1]
                name = ele[0]
        new.append((name, large))
        lst.remove((name, large))
    return new