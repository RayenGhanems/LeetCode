class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n ==0:
            return n
        n, x, s= str(n), "", 0
        for i in n:
            if i != "0":
                x+=i
                s +=int(i)

        return int(x)*s
