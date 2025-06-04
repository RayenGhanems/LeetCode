class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        x=0
        s=[]
        for i in range(len(word)):
            if word[i]>word[x]:
                x=i
            if word[i]==word[x]:
                s.append(i)
        
        l=len(word)+1-numFriends
        out= word[x:min(len(word), x+l)]

        if s:
            for x in s:
                if word[x:min(len(word), x+l)]>out:
                    out=word[x:min(len(word), x+l)]
        return out