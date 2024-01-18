class Solution(object):
    def climbStairs(self, n):
        A = (1 + math.sqrt(5)) / 2
        B = (1 - math.sqrt(5)) / 2
        fib = (pow(A, n + 1) - pow(B, n + 1)) / math.sqrt(5)

        return int(fib)
        