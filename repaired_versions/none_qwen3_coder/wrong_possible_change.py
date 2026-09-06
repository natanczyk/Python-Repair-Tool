def possible_change(coins, total):
    if total < 0:
        return 0
    if total == 0:
        return 1
    
    # Create a DP array where dp[i] represents the number of ways to make amount i
    dp = [0] * (total + 1)
    dp[0] = 1  # There's one way to make 0: use no coins
    
    # For each coin, update the dp array
    for coin in coins:
        # Update dp array from coin value to total
        for i in range(coin, total + 1):
            dp[i] += dp[i - coin]
    
    return dp[total]