def search(x, seq):
    seq = list(seq)  # Convert to list regardless of input type
    seq.append(x)
    seq.sort()  # Sort the list in place
    index = seq.index(x)
    seq.pop()  # Remove the appended element to get the original index
    return index