class Solution(object):
    def makeEqual(self, words):
        dic = defaultdict(int)
        for word in words:
            for char in word:
                dic[char] += 1
        l = len(words)
        for val in dic.values():
            if val % l != 0:
                return False
        return True
