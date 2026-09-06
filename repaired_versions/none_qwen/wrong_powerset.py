def powerset(arr):
    if arr:
        first, *rest = arr
        rest_subsets = powerset(rest)
        with_first = [[first] + subset for subset in rest_subsets]
        all_subsets = rest_subsets + with_first
        return all_subsets
    else:
        return [[]]

# Example usage:
print(powerset(['a', 'b', 'c']))