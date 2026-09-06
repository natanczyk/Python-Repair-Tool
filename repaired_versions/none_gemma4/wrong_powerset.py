def powerset(arr):
    if not arr:
        return [[]]
    
    first, *rest = arr
    rest_subsets = powerset(rest)
    # To match the example output order:
    # subsets without the first element, then subsets with the first element
    return rest_subsets + [[first] + subset for subset in rest_subsets]