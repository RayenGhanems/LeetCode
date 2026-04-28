class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l = []
        mod = grid[0][0] % x
        
        for row in grid:
            for val in row:
                if val % x != mod:
                    return -1
                l.append(val)
        
        l.sort()
        median = l[len(l)//2]
        
        return sum(abs(v - median) // x for v in l)