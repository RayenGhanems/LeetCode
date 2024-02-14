class Solution(object):
    def rearrangeArray(self, nums):
        p=[]
        n=[]
        out=[]
        for i in nums:
            if i >0:
                p.append(i)
            else:
                n.append(i)
        for i in range(len(p)):
            out.append(p[i])
            out.append(n[i])
        return out