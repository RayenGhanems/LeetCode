class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        while nums[0] < k:
            heappush(nums, 2 * heappop(nums) + heappop(nums))
            count += 1
        return count