class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k >= len(nums):
            return sum(nums)/len(nums)

        a = sum(nums[:k])
        out = a
        
        for i in range(k, len(nums)):
            a += nums[i]-nums[i-k]
            out = max(a, out)
        return out/k
        