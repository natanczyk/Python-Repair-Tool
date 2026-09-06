def powerset(arr):
    if arr:
        first, *rest = arr
        rest_subsets = powerset(rest)
        # Include subsets with first element and without first element
        return rest_subsets + [[first] + subset for subset in rest_subsets]
    else:
        return [[]]