class Solution:
    def maxArea(self, height: List[int]) -> int:
        out = 0
        i=0
        j=len(height)-1
        while(i<j):
            out = max(out,min(height[i], height[j])*(j-i))
            if(height[i]<height[j]):
                i = i+1
            else:
                j = j-1
        return out