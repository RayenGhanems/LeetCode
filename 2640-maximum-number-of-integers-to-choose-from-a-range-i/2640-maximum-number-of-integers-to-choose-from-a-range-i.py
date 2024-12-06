class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        if maxSum == 0:
            return 0
        
        out = 0
        for i in range(1,n+1):
            if i not in banned:
                maxSum -= i

                if maxSum < 0:
                    return out
                
                out+=1
        
        return out