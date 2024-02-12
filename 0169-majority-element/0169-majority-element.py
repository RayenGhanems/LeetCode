class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        sets=set(nums)
        for i in sets:
            if nums.count(i) > n/2:
                return i
        return -1
        