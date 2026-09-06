def remove_extras(lst):
    seen = set()
    return [x for x in lst if x not in seen and not seen.add(x)]