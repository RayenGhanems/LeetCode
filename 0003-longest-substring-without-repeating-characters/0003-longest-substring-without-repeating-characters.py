class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out=[]
        m=0
        for i in s:
            while i in out:
                out=out[1:]
            out+=i
            m=max(len(out),m)
        return m