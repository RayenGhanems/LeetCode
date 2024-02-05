class Solution(object):
    def firstUniqChar(self, s):
        for i,x in enumerate(s):
            if s.count(x)==1:
                return i
        return -1
        