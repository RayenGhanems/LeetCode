class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        d={}
        for i,x in enumerate(a):
            if x not in d:
                d[x]=i
        for i in range(len(nums)):
            nums[i] = d[nums[i]]
        return nums