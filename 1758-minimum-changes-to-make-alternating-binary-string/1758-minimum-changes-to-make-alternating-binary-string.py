class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        out=0
        b=s[0]
        for i in s[1:]:
            if i == b:
                out+=1
                if i == "0":
                    b ="1"
                else:
                    b='0'
            else:
                b = i
        return out if out < (len(s)+1)/2 else len(s) - out
