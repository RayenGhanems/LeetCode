class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        n=len(startTime)
        array = profit[:]
        for i in range(n):
            for j in range(n):
                if endTime[j] <= startTime[i]:
                    array[i]=max(array[i], array[j] + profit[i])
        return max(array)
