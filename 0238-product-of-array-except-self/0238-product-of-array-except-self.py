class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if nums.count(0) > 1:
            return [0]* len(nums)

        if nums.count(0) ==1:
            m = 1
            for i in nums:
                if i != 0:
                    m*= i
            out =[0] * len(nums)
            out[nums.index(0)] = m
            return out                    


        m = 1
        for i in nums:
            m*= i
        out =[]
        for i in nums:
            out.append(int(m/i))
        return out