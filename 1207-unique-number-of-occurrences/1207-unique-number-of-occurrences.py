class Solution(object):
    def uniqueOccurrences(self, arr):
        count = {}
        for i in arr:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        seen_counts = set()
        for value in count.values():
            if value in seen_counts:
                return False
            seen_counts.add(value)
        return True

        