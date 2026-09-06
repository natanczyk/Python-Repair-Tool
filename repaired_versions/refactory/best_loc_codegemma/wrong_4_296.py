def sort_age(lst):
    output = []
    while lst:
        max_age = max(lst, key=lambda item: item[1])
        output.append(max_age)
        lst.remove(max_age)
    return output