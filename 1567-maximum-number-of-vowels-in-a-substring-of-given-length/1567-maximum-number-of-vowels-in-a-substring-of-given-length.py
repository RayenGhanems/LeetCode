class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s = list(s)
        v = {'a', 'e', 'i', 'o', 'u'}
        a = 0

        if k >= len(s):
            for i in s:
                if i in v:
                    a+=1
            return a

        for i in range(k):
            if s[i] in v:
                a+=1
        
        out = a
        
        for i in range(k,len(s)):
            if s[i-k] in v:
                a-=1
            if s[i] in v:
                a+=1
            out = max(a, out)
        return out