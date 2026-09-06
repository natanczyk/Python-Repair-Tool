def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    enumerated_list = []
    for i, elem in enumerate(seq):
        enumerated_list.append((i, elem))

    if not enumerated_list:
        return 0

    for number in enumerated_list:
        if x <= number[1]:
            return number[0]
    return len(seq)