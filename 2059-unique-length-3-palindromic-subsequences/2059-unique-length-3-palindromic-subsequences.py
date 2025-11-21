class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        # For each possible outer character
        for c in map(chr, range(ord('a'), ord('z') + 1)):
            first = s.find(c)
            last = s.rfind(c)
            if first != -1 and last - first >= 2:
                middle_chars = set(s[first + 1:last])
                res += len(middle_chars)
        return res
