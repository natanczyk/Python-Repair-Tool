def remove_extras(lst):
    output = []
    count = {}
    for entry in lst:
        if entry not in count:
            count[entry] = 0
        if count[entry] == 0:
            output.append(entry)
            count[entry] += 1
    return output