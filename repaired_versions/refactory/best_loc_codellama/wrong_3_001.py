def remove_extras(input_list):
    output = []
    for element in input_list:
        if element not in output:
            output.append(element)
    return output