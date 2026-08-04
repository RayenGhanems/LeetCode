class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n,x = nums[0],nums[-1]
        nums = set(nums)
        out=[]
        for i in range(n,x):
            if i not in nums:
                out.append(i)
        return out
        