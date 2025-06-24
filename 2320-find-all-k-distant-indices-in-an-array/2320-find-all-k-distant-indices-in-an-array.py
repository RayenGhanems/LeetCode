class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l = set()
        for i in range(len(nums)):
            if nums[i]== key:
                l.add(i)
                for j in range(k+1):
                    if i-j>=0:
                        l.add(i-j)
                    if j+i<len(nums):
                        l.add(i+j)

        return list(l)

        