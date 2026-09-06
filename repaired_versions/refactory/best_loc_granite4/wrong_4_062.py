def sort_age(lst):
    final = []
    while lst:
        old = max(lst, key=lambda x: x[1])
        final.append(old)
        lst.remove(old)
    return final