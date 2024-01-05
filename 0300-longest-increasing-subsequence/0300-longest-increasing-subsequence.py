class Solution(object):
    def lengthOfLIS(self, nums):
        array=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    array[i]=max(array[i],array[j]+1)
        return max(array)
                    
        