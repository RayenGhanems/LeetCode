class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        out = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    out = max(out, nums[j] - nums[i])

        return out