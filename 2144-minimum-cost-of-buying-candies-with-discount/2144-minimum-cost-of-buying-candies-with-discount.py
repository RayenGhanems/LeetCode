class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        out = 0
        for i in range(len(cost)):
            if (i+1) %3 !=0 :
                out +=cost[i]
                print(i, cost[i])
        return out

