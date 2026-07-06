class Solution:
    def removeCoveredIntervals(self, l: List[List[int]]) -> int:
        l = sorted(l, key= lambda x: (x[0], -x[1]))
        pj,out = l[0][1], 0
        for i,j in l[1:]:
            if pj >= j:
                out+=1
            else:
                pj = j
        return len(l)-out
