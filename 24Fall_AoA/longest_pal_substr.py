def longest_pal_substr(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    max_len = 0 if n == 0 else 1
    pal_start = 0
    
    for i in range(n):
        dp[i][i] = True
    
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            max_len = 2
            pal_start = i
    
    for sub_length in range(3,n+1):
        for i in range(n-sub_length+1):
            j = sub_length + i-1
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                if max_len<sub_length:
                    max_len = sub_length
    
    return s[pal_start:pal_start+max_len]
