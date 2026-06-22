class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        D = {}
        for c in "balon":
            D[c] = 0
        for c in text:
            if c in D:
                D[c] += 1
        D["l"] /= 2
        D["o"] /= 2
        return int(min(D.values()))
        