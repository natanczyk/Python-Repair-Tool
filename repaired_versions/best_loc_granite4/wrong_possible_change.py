from functools import lru_cache

def possible_change(coins, total):
    @lru_cache(None)
    def count_ways(remaining, idx):
        if remaining == 0:
            return 1
        if remaining < 0 or idx >= len(coins):
            return 0
        # use coin[idx] or skip it
        return count_ways(remaining - coins[idx], idx) + count_ways(remaining, idx + 1)

    return count_ways(total, 0)