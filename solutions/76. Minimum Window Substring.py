class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        to_fulfill = len(t_count)
        window = {}
        l = 0
        min_length = len(s)
        res = ""
        for r, c in enumerate(s):
            if c in t_count:
                window[c] = window.get(c, 0) + 1
                if window[c] == t_count[c]:
                    to_fulfill -= 1
            while to_fulfill == 0:
                if r - l + 1 <= min_length:
                    min_length = r - l + 1
                    res = s[l:r+1]
                if s[l] in t_count:
                    window[s[l]] = window[s[l]] - 1
                    if window[s[l]] < t_count[s[l]]:
                        to_fulfill += 1
                l += 1
        return res
