def remove_extras(input_list):
    result = []
    for ele in input_list:
        if ele not in result:
            result.append(ele)
    return result