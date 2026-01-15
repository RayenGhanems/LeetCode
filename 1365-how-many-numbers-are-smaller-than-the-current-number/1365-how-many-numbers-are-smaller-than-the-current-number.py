class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        for i in range(len(nums)):
            nums[i]=a.index(nums[i])
        return nums