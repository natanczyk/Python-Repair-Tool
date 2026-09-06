def remove_extras(lst):
    # We create a new list to avoid modifying the list while iterating over it
    # and to ensure we return a new list as requested.
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

def remove_multiple(n, lst):
    # This helper function is kept for structural consistency with the original code,
    # although the logic in remove_extras now handles the task more efficiently.
    if lst.count(n) <= 1:
        return lst
    else:
        # To remove only the later occurrences, we reverse, remove the first found, then reverse back.
        lst.reverse()
        lst.remove(n)
        lst.reverse()
        return remove_multiple(n, lst)