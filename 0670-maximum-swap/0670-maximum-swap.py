class Solution:
    def maximumSwap(self, num: int) -> int:
        out = [int(digit) for digit in str(num)]
        sorted_out = sorted(out, reverse=True)
        for b in range(len(out)):
            if out[b] != sorted_out[b]:
                i = len(out) - 1 - out[::-1].index(sorted_out[b])
                out[b], out[i] = out[i], out[b]
                break
        return int(''.join(map(str, out)))
