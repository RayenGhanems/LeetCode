class Solution(object):
    def minPairSum(self, nums):

        # Sorting the array
        sorted_array = sorted(nums)

        # Initiating two pointers L and R
        l = 0 # Points to first item in the array
        r = len(nums) - 1 # Points to last item in the array
 
        maximum = 0

        for i in range(int(len(nums) / 2)):
            my_sum = sorted_array[l] + sorted_array[r]
            maximum =max(maximum,my_sum) 
            l += 1
            r -= 1

        return maximum

        