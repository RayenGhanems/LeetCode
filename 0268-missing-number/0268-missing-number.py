class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = 0
        for i,x in enumerate(nums):
            if i != x:
                return i
            n+=1
        return n