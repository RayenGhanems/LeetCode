class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        out=[]
        for i in range(len(nums)/3):
            num=nums[i*3:i*3+3]
            if num[-1]-num[0] > k:
                return []
            out.append(num)
        return out   