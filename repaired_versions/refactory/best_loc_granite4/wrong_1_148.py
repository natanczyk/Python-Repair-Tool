def search(val, seq):
    if not seq:  # Handle empty sequence
        return 0
    if val <= seq[0]:
        position = 0
    elif val > seq[-1]:  # Change >= to >
        position = len(seq)
    else:
        for i, item in enumerate(seq):
            if val <= item:
                position = i
                break
        else:
            position = len(seq)  # Fallback if no break occurred
    return position