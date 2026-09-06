def search(x, seq):
    if type(seq) == tuple:
        seq = list(seq)
        seq.append(x)
        seq = sorted(seq)
        return seq.index(x)
        
    elif type(seq) == list:
        # Create a copy to avoid modifying the original list passed as an argument
        temp_seq = list(seq)
        temp_seq.append(x)
        temp_seq = sorted(temp_seq)
        return temp_seq.index(x)