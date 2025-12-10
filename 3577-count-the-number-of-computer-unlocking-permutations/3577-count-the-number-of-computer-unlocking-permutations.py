class Solution:
    def countPermutations(self, com: List[int]) -> int:

        def factorial(x:int)-> int:
            if x == 1:
                return 1
            return x * factorial(x-1)

        if com[0] >= min(com[1:]):
            return 0
            
        return factorial(len(com) -1) % ((10**9)+7)
        