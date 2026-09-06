def remove_extras(lst):
    output = []
    for entry in lst:
        if entry not in output:
            output.append(entry)
    return output