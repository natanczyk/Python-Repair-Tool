def remove_extras(lst):
    """
    Returns a new list with all repeated occurrences of any element removed,
    keeping the first occurrence of each element.
    """
    def helper(remaining, seen):
        if not remaining:
            return []
        first = remaining[0]
        if first in seen:
            return helper(remaining[1:], seen)
        else:
            seen.add(first)
            return [first] + helper(remaining[1:], seen)

    return helper(lst, set())