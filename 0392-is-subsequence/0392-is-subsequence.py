class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        t = list(t)
        s = list(s) 
        i = 0
        for c in t:
            if c == s[i]:
                i+=1
                if i == len(s):
                    return True
        return False
        