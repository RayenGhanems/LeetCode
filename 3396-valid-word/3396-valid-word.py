class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        vowels={"a","A","e","E",'i','I','o','O','u','U'}
        numbers={'0','1','2','3','4','5','6','7','8','9'}
        s= {'g','v','k','O','u','x','I','P','Y','f','w','n','A','y','M','j','W','N','b','X','U','H','a','h','G','T','z','B','o','e','l','m','q','R','V','Q','L','2','D','i','d','r','p','Z','F','t','S','K','C','s','J','E','c'}

        v,c=False,False

        for x,i in enumerate(word):
            if i not in s and i not in numbers:
                return False
            if i in vowels:
                v=True
            elif i not in numbers:
                c=True
            if v==c and v==True:
                for i in word[x:]:
                    if i not in s and i not in numbers:
                        return False
                return True
        return False

        