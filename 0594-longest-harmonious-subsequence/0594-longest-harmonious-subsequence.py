from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        out = 0
        for i in counter.keys():
            if i-1 in counter:
                out= max(out,counter[i]+counter[i-1])
            elif i+1 in counter:
                out= max(out,counter[i]+counter[i+1])
        return out

        