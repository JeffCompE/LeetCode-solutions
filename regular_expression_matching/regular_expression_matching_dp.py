class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [(len(p) + 1) * [False] for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True
        for s_index in range(len(s), -1, -1):
            for p_index in range(len(p) - 1, -1, -1):
                if p[p_index] == '*':
                    continue
                firstmatch = True if s_index < len(s) and p[p_index] in {s[s_index], '.'} else False
                if p_index + 1 < len(p) and p[p_index + 1] == '*':
                    dp[s_index][p_index] = dp[s_index][p_index + 2] or (firstmatch and dp[s_index + 1][p_index])
                else:
                    result = firstmatch and dp[s_index + 1][p_index + 1]
                    dp[s_index][p_index] = result

        return dp[0][0]
