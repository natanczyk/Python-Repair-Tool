def remove_extras(input_list):
    seen = set()
    result = []
    for element in input_list:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result