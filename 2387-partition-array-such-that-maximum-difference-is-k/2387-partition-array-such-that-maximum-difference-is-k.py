class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))
        out = 1
        j=nums[0]
        for i in nums[1:]:
            if i-j>k:
                j=i
                out+=1
        return out