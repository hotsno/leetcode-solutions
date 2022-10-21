class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == '0':
                if i == len(s) - 1:
                    dp[i] = 0
                else:
                    dp[i] = dp[i + 1]
            elif i == len(s) - 1:
                dp[i] = 1
            else:
                dp[i] = dp[i + 1]
                if int(c + s[i + 1]) <= 26:
                    dp[i] += 1
                    if i + 2 < len(s) - 1:
                        dp[i] += dp[i + 2]
        return dp[0]
