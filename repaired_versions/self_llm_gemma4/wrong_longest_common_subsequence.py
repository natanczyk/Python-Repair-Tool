def longest_common_subsequence(a, b):
    memo = {}

    def helper(s1, s2):
        state = (s1, s2)
        if state in memo:
            return memo[state]
        
        if not s1 or not s2:
            return ''

        if s1[0] == s2[0]:
            result = s1[0] + helper(s1[1:], s2[1:])
        else:
            res1 = helper(s1, s2[1:])
            res2 = helper(s1[1:], s2)
            result = res1 if len(res1) >= len(res2) else res2
            
        memo[state] = result
        return result

    return helper(a, b)