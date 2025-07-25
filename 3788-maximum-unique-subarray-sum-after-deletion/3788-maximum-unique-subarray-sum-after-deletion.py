class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums = sorted(nums)
        if nums[0]>0:
            return sum(set(nums))
        elif nums[-1]<=0:
            return nums[-1]
        s = set(nums)
        out=-200
        for i in s:
            out = max(out, out+i,i)
        return out

        

        