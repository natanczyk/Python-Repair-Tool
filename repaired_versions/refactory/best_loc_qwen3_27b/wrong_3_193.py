def remove_extras(lst):
    # We want to keep the first occurrence of each element and remove subsequent duplicates.
    # The original buggy code tried to reverse the list and remove from the end,
    # but lst.reverse() returns None, causing issues.
    
    # A simpler approach: iterate through the list and keep only the first occurrence of each element.
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen