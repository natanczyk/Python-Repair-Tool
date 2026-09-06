def search(x, seq):
    if not seq:  # Handles both empty lists and empty tuples
        return 0
    else:
        for i in range(len(seq)):
            if x <= seq[i]:  # Combine the conditions for x < seq[i] and x == seq[i]
                return i
        return len(seq)  # Return the length of seq if x is greater than all elements