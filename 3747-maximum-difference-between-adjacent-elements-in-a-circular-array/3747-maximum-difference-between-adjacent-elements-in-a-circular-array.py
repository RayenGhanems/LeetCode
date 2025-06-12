class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        out = abs(nums[0]-nums[-1])
        for i in range(1,len(nums)):
            out=max(out,abs(nums[i]-nums[i-1]))
        return out
        