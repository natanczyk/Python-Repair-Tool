def lcs_length(s, t):
    from collections import Counter

    dp = Counter()
    max_len = 0

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                # The length of the common substring ending at i, j 
                # is 1 + the length of the common substring ending at i-1, j-1
                val = dp[i - 1, j - 1] + 1
                dp[i, j] = val
                if val > max_len:
                    max_len = val

    return max_len