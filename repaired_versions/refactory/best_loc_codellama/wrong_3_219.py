def remove_extras(input_list):
    seen = set()
    return [x for x in input_list if x not in seen and not seen.add(x)]