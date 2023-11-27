class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums, reverse=True)
        i,j,m,output=0,1,1,0

        while nums[i] != nums[-1]:
            while nums[i] == nums[j]:
                j+=1
                m+=1
            output+= m
            i=j
        return output



        