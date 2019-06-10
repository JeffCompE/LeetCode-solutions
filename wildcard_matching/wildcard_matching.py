class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]

        dp[len(s)][len(p)] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                firstmatch = True if (i < len(s) and p[j] in {'?', '*', s[i]}) else False
                if p[j] == '*':
                    if j < len(p):
                        dp[i][j] =  (firstmatch and dp[i + 1][j]) or dp[i][j + 1]
                else:
                    dp[i][j] = firstmatch and dp[i + 1][j + 1]
        return dp[0][0]
    
