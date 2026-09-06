# Python 3
def possible_change(coins, total):
    memo = {}

    def helper(coins, total):
        key = (total, tuple(coins))
        if key in memo:
            return memo[key]

        if total == 0:
            return 1
        if total < 0 or not coins:
            return 0

        first, *rest = coins
        result = helper(coins, total - first) + helper(rest, total)
        memo[key] = result
        return result

    return helper(coins, total)