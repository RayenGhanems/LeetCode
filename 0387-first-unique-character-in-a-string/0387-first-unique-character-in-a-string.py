class Solution(object):
    def firstUniqChar(self, s):
        l=""
        for i,x in enumerate(s):
            if x not in l and s.count(x)==1:
                return i
            l+=x
        return -1
        