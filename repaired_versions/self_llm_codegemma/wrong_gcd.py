def gcd(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    elif a < 0:
        return gcd(-a, b)
    elif b < 0:
        return gcd(a, -b)
    elif a == b:
        return a
    else:
        return gcd(b, a % b)