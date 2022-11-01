class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        impossible = set()
        def canBeSplit(si): # si = starting index
            if si >= len(s):
                return True
            if si in impossible:
                return False
            cur = ""
            for i in range(si, len(s)):
                cur += s[i]
                if cur in wordSet and canBeSplit(i + 1):
                    return True
            impossible.add(si)
            return False
        return canBeSplit(0)

    def wordBreak2(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
