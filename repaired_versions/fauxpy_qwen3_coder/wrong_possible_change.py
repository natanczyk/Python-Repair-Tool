# Python 3
def possible_change(coins, total):
    # Memoization cache
    memo = {}
    
    def helper(coins_tuple, remaining):
        if remaining == 0:
            return 1
        if remaining < 0 or not coins_tuple:
            return 0
        
        # Check if already computed
        if (coins_tuple, remaining) in memo:
            return memo[(coins_tuple, remaining)]
        
        # Take the first coin and use it, or skip it
        first_coin = coins_tuple[0]
        rest_coins = coins_tuple[1:]
        
        # Use first coin (can use multiple times) or skip it
        result = helper(coins_tuple, remaining - first_coin) + helper(rest_coins, remaining)
        memo[(coins_tuple, remaining)] = result
        return result
    
    return helper(tuple(coins), total)