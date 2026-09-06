# Python 3
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0 or not coins:
        return 0

    first, *rest = coins
    # Either use the first coin (and keep considering it) or skip it
    return possible_change(coins, total - first) + possible_change(rest, total)