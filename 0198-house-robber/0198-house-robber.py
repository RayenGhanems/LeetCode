class Solution(object):
    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums)
        
        dp = {}
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i, x in enumerate(nums[2:], start=2):
            dp[i] = x + max(dp[j] for j in range(i-1))

        return max(dp.values())


        
        