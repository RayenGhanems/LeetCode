class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = list(set(arr))
        a.sort()
        d = {}
        out = []
        for i in range(len(a)):
            d[a[i]] = i
        for i in range(len(arr)):
            out.append(d[arr[i]]+1)
        return out
        