def search(x, seq):
    # Convert the sequence to a list to allow modification
    seq_list = list(seq)
    # Append the target value to the list
    seq_list.append(x)
    # Sort the list in place
    seq_list.sort()
    # Return the index of the first occurrence of x
    return seq_list.index(x)