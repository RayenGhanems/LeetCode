class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j,n= 0,1,len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return [n-2,n-1]