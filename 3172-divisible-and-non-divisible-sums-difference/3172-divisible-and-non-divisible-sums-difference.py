class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n+=1
        o,t=0,0
        for i in range(n):
            o+=i
        i=m

        if i<=n-1:
            while i<n:
                o-=2*i
                i+=m
        return o-t


        