def powerset(arr):
    if arr:
        first, *rest = arr
        rest_subsets = powerset(rest)
        # Include subsets that don't contain the first element
        # and subsets that do contain the first element
        return rest_subsets + [[first] + subset for subset in rest_subsets]
    else:
        return [[]]