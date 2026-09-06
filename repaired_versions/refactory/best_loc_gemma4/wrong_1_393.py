def search(x, seq):
    if type(seq) == tuple:
        seq = list(seq)
        seq.append(x)
        a = sorted(seq)
        return a.index(x)
        
    elif type(seq) == list:
        seq = list(seq) # Create a copy to avoid modifying the original list
        seq.append(x)
        seq.sort() # Sort the list in place
        return seq.index(x)