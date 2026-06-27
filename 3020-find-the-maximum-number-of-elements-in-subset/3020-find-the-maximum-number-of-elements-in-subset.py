from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        D = Counter(nums)

        ans = 1

        if 1 in D:
            ans = max(ans, D[1] if D[1] % 2 else D[1] - 1)

        for x in D:
            if x == 1:
                continue

            cur = x
            length = 0

            while cur in D:
                if D[cur] >= 2:
                    length += 2
                    cur = cur * cur
                else:
                    length += 1
                    break

            if length % 2 == 0:
                length -= 1

            ans = max(ans, length)

        return ans