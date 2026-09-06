def remove_extras(values):
    output = []
    seen = set()  # Initialize seen as an empty set
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)  # Add the value to seen to track duplicates
    return output