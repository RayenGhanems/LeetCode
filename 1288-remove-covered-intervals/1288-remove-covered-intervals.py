class Solution:
    def removeCoveredIntervals(self, l: List[List[int]]) -> int:
        l.sort(key=lambda x: (x[0], -x[1]))  # In-place sort (O(1) auxiliary space)
        pj, out = l[0][1], 0
        for idx in range(1, len(l)):         # No slicing
            _, j = l[idx]
            if pj >= j:
                out += 1
            else:
                pj = j
        return len(l) - out