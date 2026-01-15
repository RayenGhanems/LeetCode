class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,x in enumerate(nums):
            s = target - x
            if s in d:
                return [i,d[s]]
            d[x] = i
        return [-1]