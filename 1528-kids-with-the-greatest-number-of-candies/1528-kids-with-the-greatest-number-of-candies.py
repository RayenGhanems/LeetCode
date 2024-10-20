class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out =[]
        m = max(candies)
        n = min(candies)
        if extraCandies + n >= m:
            return [True]*len(candies)
        for i in candies:
            if i + extraCandies >= m:
                out.append(True)
            else:
                out.append(False)
        return out