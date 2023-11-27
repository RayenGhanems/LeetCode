class Solution:
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        if t < abs(sx - fx) or t < abs(sy - fy):
            return False
        
        if abs(sx - fx) == abs(sy - fy) and abs(sy - fy) == 0:
            if t == 1:
                return False
        
        return True
