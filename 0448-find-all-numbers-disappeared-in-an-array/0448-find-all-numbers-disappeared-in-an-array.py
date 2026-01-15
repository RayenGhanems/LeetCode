class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        out = []
        for i in range(len(nums)):
            if i+1 not in s:
                out.append(i+1)
        return out
        