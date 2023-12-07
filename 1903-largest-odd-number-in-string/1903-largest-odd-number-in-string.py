class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num) - 1, -1, -1):
            if num[i] not in "24680":
                return num[:i+1]
        return ""