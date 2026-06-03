class Solution:
    def plusOne(self, dg: List[int]) -> List[int]:
        for i in range(len(dg)-1,-1,-1):
            if dg[i]==9:
                dg[i]=0
            else:
                dg[i]+=1
                return dg
        dg.insert(0,1)
        return dg