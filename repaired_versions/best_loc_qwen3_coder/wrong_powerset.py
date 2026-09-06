def powerset(arr):
    if arr:
        first, *rest = arr
        rest_subsets = powerset(rest)
        # Return both subsets that include 'first' and those that don't
        return rest_subsets + [[first] + subset for subset in rest_subsets]
    else:
        return [[]]