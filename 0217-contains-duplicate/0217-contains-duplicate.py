class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        x = nums[0]
        for i in nums[1:]:
            if i ==x:
                return True
            x=i
        return False

        