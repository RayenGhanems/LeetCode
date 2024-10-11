class Solution:
    def maxArea(self, height: List[int]) -> int:
        out = 0
        i=0
        j=len(height)-1
        while(i<j):
            m = min(height[i], height[j])
            out = max(out,m*(j-i))
            if(height[i]<height[j]):
                i = i+1
            else:
                j = j-1
        return out