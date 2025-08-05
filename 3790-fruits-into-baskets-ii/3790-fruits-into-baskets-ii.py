class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        out = 0
        for i in range(len(fruits)):
            j=0
            while j<len(fruits)-1 and  fruits[i]>baskets[j]:
                j+=1
            if fruits[i]>baskets[j]:
                out+=1
            else:
                baskets[j]=-1
        return out
        