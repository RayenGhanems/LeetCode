class Solution:
    def countPermutations(self, com: List[int]) -> int:

        def factorial(x:int)-> int:
            if x == 1:
                return 1
            return x * factorial(x-1)
        x=com[0]
        for i in com[1:]:
            if i<= x:
                return 0

        return factorial(len(com) -1) % ((10**9)+7)
        