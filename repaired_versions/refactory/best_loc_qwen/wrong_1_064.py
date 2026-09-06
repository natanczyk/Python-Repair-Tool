def search(x, seq):
    if type(seq) == tuple:
        seq = list(seq)
        seq.append(x)
        seq.sort()  # Corrected from sorted(seq) to seq.sort()
        return seq.index(x)
        
    elif type(seq) == list:
        seq.append(x)
        seq.sort()  # Corrected from sorted(seq) to seq.sort()
        return seq.index(x)