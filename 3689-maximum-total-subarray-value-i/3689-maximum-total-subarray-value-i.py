class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m,n = nums[0],nums[0]
        for i in nums:
            if i>m:
                m=i
            elif i <n:
                n=i
        return k*(m-n)