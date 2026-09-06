def remove_extras(input_list):
    result = []
    for element in input_list:
        if element not in result:
            result.append(element)
    return result