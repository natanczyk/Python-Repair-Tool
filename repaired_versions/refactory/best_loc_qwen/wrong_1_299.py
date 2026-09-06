def search(x, seq):
    no = len(seq)  # Initialize no outside the loop
    for i in range(len(seq)):
        if x > seq[i]:
            continue
        elif x <= seq[i]:
            no = i
            break
    return no