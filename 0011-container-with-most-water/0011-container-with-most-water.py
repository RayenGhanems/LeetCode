class Solution:
    def maxArea(self, h: List[int]) -> int:
        r,l,m = 0, len(h)-1 ,0
        while r!=l:
            m=max(m,(min(h[r],h[l])*(l-r)))
            if h[r]<h[l]:
                r+=1
            else:
                l-=1
        return m