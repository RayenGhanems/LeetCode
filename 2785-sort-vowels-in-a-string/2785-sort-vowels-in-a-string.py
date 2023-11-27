class Solution(object):
    def sortVowels(self, s):
        return ''.join((qu.popleft() if char in 'AEIOUaeiou' else char) for char, qu in zip(s, [deque(sorted(char for char in s if char in 'AEIOUaeiou'))]*len(s)))