class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n+=1
        o,t=0,0
        if n <m:
            for i in range(n):
                o+=i
            
        else:
            for i in range(n):
                if i%m==0:
                    t+=i
                else:
                    o+=i
        return o -t
        


        