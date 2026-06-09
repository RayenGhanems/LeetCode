class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m,n = 0, 10**9
        for i in nums:
            if i>m:
                m=i
            if i <n:
                n=i
        return k*(m-n)