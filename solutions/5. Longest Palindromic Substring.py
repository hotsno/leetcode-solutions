class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome_length(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return (l + 1, r - 1)

        longest, longest_l, longest_r = 1, 0, 0
        for i in range(len(s)):
            offsets = [[-1, 1], [-1, 0]]
            for offset in offsets:
                l, r = palindrome_length(i + offset[0], i + offset[1])
                if l - r + 1 > longest:
                    longest, longest_l, longest_r = l - r + 1, l, r

        return s[longest_l:longest_r + 1]
