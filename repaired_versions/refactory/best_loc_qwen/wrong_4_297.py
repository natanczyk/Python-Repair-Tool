def sort_age(lst):
    output = []
    while lst:
        max_age = max(lst, key=lambda x: x[1])[1]
        for item in lst:
            if item[1] == max_age:
                output.append(item)
                lst.remove(item)
                break
    return output