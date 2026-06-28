class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        j = 1
        for i in arr[1:]:
            if i >= j+1:
                j +=1
        return j 
        