class Solution(object):
    def minSteps(self, s, t):
        dicts={}
        out=0
        for char in s:
            if char in dicts:
                dicts[char]+=1
            else:
                dicts[char]=1
        for char in t:
            if char in dicts and dicts[char]>0:
                dicts[char]-=1
        for i in dicts.values():
            out+=i
        return out