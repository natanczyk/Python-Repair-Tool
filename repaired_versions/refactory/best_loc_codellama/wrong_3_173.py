def remove_extras(input_list):
    seen = set()
    result = []
    for x in input_list:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result