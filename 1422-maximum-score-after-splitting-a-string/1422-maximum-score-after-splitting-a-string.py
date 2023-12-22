class Solution(object):
    def maxScore(self, s):
        out=0
        for i in range(1,len(s)):
            out=max(out,s[:i].count('0')+s[i:].count('1'))
        return out