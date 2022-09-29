class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindromes(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res, l , r = res + 1, l - 1, r + 1
            return res

        res = 0
        for i in range(len(s)):
            res += count_palindromes(i, i) + count_palindromes(i - 1, i)
        return res
