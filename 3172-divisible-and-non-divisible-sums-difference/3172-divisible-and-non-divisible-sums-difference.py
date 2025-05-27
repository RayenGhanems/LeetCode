class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n+=1
        o=0
        for i in range(n):
            if i%m==0:
                o-=i
            else:
                o+=i
        
        return o


        