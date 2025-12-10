class Solution:
    def countPermutations(self, com: List[int]) -> int:

        if com[0] >= min(com[1:]):
            return 0
            
        return factorial(len(com) -1) % ((10**9)+7)
        