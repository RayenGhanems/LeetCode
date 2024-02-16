from collections import Counter

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        freq_map = Counter(arr)
        frequencies = list(freq_map.values())
        heapq.heapify(frequencies)
        elements_removed = 0
        while frequencies:
            elements_removed += heapq.heappop(frequencies)
            if elements_removed > k:
                return len(frequencies) + 1
        return 0