class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x = str(x)
        for i in range(int(len(x)/2)):
            if x[i]!= x[-(i+1)]:
                return False
        return True