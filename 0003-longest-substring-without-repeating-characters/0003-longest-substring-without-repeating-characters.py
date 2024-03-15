class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out=[]
        m=0
        for i in s:
            m=max(len(out),m)
            while i in out:
                out=out[1:]
            out+=i
        return max(m,len(out))