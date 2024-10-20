class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if nums.count(0) > 1:
            return [0]* len(nums)
        if nums.count(0) ==1:
            m = 1
            for i in nums:
                if i != 0:
                    m*= i
            out =[]
            for i in nums:
                if i != 0 :
                    out.append(0)
                else:
                    out.append(int(m))
            return out                    


        m = 1
        for i in nums:
            m*= i
        out =[]
        for i in nums:
            if i != 0 :
                out.append(int(m/i))
            else:
                out.append(int(m))
        return out