class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        dic={}
        out=-1
        for i,char in enumerate(s):
            if char in dic:
                out=max(out,i-dic[char]-1)
            else :
                dic[char]=i
        return out