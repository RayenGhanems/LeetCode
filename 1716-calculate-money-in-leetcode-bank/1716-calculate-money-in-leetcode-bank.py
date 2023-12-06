class Solution(object):
    def totalMoney(self, n):
        i,out=1,0
        while i <=(n//7):
            out+=28+7*(i-1)
            i+=1
        return out + i*(n%7) + sum(range(0,n%7))