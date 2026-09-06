def remove_extras(input_list):
    seen = set()
    result = []
    for element in input_list:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result