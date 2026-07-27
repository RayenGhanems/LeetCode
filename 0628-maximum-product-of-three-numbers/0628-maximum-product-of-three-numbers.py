class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        mx,mx1,mx2,mn,mn1 = -1001,-1001,-1001,1001,1001
        for i in nums:
            if i>mx:
                mx2,mx1,mx=mx1,mx,i
            elif i>mx1:
                mx2,mx1=mx1,i
            elif i>mx2:
                mx2 = i
            
            if i<mn:
                mn1,mn=mn,i
            elif i<mn1:
                mn1=i

        return max(mn*mn1*mx,mx*mx1*mx2)
