class Solution:
    def countPermutations(self, com: List[int]) -> int:
        l =len(com)
        x=com[0]
        for i in com[1:]:
            if i<= x:
                return 0
        out =1
        for i in range(2,l):
            out=out*i
        return out % ((10**9)+7)



        