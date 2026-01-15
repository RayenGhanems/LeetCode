class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a =set(nums)
        n = len(nums)
        for i in range(n):
            if i not in a:
                return i
        return n