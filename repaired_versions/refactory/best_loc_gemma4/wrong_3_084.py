def remove_extras(lst):
    if not lst:
        return []
    
    # To keep the first occurrence and remove subsequent duplicates,
    # we check if the first element is the first time it appears in the list.
    # Since we are processing from the start, we only keep lst[0] if it 
    # doesn't appear in the part of the list we've already processed.
    # However, the simplest recursive way to maintain the "first occurrence" 
    # rule without a helper is to filter the rest of the list.
    
    first = lst[0]
    rest = lst[1:]
    # Remove all occurrences of 'first' from the rest of the list
    filtered_rest = [x for x in rest if x != first]
    
    return [first] + remove_extras(filtered_rest)