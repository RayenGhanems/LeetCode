class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = grid[0][0]%x
        L = []
        for l in grid:
            for i in l:
                if i %x != a:
                    return -1
                L.append(i)
        L.sort()
        midle = L[int(len(L)/2)]
        out = 0
        for i in L:
            out += abs(i-midle)
        return int(out/x)

        