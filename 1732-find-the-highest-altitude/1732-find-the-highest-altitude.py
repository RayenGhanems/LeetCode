class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        out = h
        for i in gain:
            h += i
            out = max(out, h)
        return max(out, h)
            