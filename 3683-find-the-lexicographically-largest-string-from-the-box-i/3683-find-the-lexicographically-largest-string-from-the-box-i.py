class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        x,s=0,[]
        for i in range(len(word)):
            if word[i]>=word[x]:
                if word[i]==word[x]:
                    s.append(i)
                else:
                    x=i
                    s=[]

        l=len(word)+1-numFriends
        out= word[x:min(len(word), x+l)]
        if s:
            for x in s:
                if word[x:min(len(word), x+l)]>out:
                    out=word[x:min(len(word), x+l)]
        return out