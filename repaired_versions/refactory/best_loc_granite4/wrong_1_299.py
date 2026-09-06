def search(x, seq):
    no = len(seq)  # Initialize no before the loop
    for i in range(0, len(seq)):
        if x > seq[i]:
            continue
        elif x <= seq[i]:
            no = i
            break
    return no