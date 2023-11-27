class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr)==1:
            return 1
        arr.sort()
        arr[0]=1
        left = 1
        for right in arr[1:]:
            if (right - left) >1:
                right =left +1
            left = right
        return right
        