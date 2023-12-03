class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        i,j=points[0]
        time =0
        for point in points[1:]:
            x,y=point
            time +=max(abs(x-i),abs(y-j))
            i,j=x,y
        return time