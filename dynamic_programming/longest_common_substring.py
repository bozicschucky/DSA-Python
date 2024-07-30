
def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    max_len = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
    return max_len


s1 = "ABABC"
s2 = "BABCA"

print(longest_common_substring(s1, s2))  # 3

s1 = "vista"
s2 = "hish"

print(longest_common_substring(s1, s2))  # 2
