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
            if x*i>0:
                t=abs(x-i)
            else:
                t=abs(x-i)
            if y*j>0:
                t=max(t,abs(y-j))
            else:
                t=max(t,abs(j-y))
            time +=t
            i,j=x,y
        return time