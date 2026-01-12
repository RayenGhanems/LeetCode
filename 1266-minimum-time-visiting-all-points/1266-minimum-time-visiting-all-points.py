class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        out = 0
        p = points[0]
        for point in points[1:]:
            t=max(abs(p[0]-point[0]), abs(p[1]-point[1]))
            out += t
            p=point
        return out
        