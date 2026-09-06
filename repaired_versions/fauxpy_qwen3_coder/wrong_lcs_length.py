def lcs_length(s, t):
    if not s or not t:
        return 0
    
    m, n = len(s), len(t)
    # Create a 2D DP table
    dp = [[0] * n for _ in range(m)]
    
    max_length = 0
    
    # Fill the DP table
    for i in range(m):
        for j in range(n):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])
    
    return max_length