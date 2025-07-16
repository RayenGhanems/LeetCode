class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = sum(1 for x in nums if x % 2 == 0)
        odd = len(nums)-even

        eve, od = 0,0
        for i in nums:
            if i %2 ==0:
                eve = max(eve,od+1)
            else:
                od = max(od, eve+1)

        return max(even, odd, eve, od)

                    


        