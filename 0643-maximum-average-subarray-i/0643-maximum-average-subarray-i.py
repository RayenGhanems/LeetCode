class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        out = sum(nums[:k])
        print(out)
        av = out
        for i in range(len(nums)-k):
            out = out -nums[i] + nums[i+k]
            av = max(av, out)
        return av/k