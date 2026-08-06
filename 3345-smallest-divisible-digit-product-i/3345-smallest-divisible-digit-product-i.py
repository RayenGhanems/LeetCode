class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def s(x:int) -> int:
            if x<10:
                return x
            s=str(x)
            out=int(s[0])
            for i in s[1:]:
                out*=int(i)
            return out
        for i in range(n,n+t+1):
            m = s(i)%t
            if m==0:
                return i
        return -1
        