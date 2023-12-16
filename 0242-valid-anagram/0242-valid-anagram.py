class Solution(object):
    def isAnagram(self, s, t):
        dict ={}
        for char in s:
            if char not in dict:
                dict[char]=1
            else:
                dict[char]+=1
        for char in t:
            if char not in dict:
                return 0
            else :
                dict[char]-=1
                if dict[char]==0:
                    del dict[char]
        return not dict