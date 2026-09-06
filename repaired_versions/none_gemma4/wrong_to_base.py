import string

def to_base(num, b):
    result = ''
    alphabet = string.digits + string.ascii_uppercase
    while num > 0:
        i = num % b
        num = num // b
        # The bug was appending the remainder to the end of the string.
        # Base conversion remainders are generated from least significant to most significant.
        # Therefore, the new digit must be prepended to the result.
        result = alphabet[i] + result
    return result