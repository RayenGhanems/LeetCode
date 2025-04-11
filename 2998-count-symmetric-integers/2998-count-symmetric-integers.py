class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        out = 0
        for i in range(low, high + 1):  # include high
            s = str(i)
            if len(s) % 2 == 0:
                m = len(s) // 2
                if sum(map(int, s[:m])) == sum(map(int, s[m:])):
                    out += 1
        return out
