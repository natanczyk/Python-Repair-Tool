def sort_age(lst):
    output = []
    for person in lst:
        output.append(person)
    output.sort(key=lambda x: x[1], reverse=True)
    return output