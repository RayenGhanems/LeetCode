class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        one=""
        two=""
        for i in word1:
            one+=i
        for i in word2:
            two +=i
        return one == two  