class Solution(object):
    def makeEqual(self, words):
        dic = {chr(letter): 0 for letter in range(ord('a'), ord('z') + 1)}
        for word in words:
            for char in word:
                dic[char] += 1
        l = len(words)
        for letter in range(ord('a'), ord('z') + 1):
            if dic[chr(letter)] % l != 0:
                return False
        return True
