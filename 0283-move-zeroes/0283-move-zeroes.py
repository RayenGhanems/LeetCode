class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = nums.count(0)
        for i in range(n):
            nums.pop(nums.index(0))
            nums.append(0)
        return nums
        