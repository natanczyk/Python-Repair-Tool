def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if not coins:
        return 0
    first = coins[0]
    if total >= first:
        return possible_change(coins, total - first) + possible_change(coins[1:], total)
    else:
        return possible_change(coins[1:], total)