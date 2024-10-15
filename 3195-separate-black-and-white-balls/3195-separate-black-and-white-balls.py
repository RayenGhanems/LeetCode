class Solution:
    def minimumSteps(self, s: str) -> int:
        white=0
        out=0
        j=0
        n=len(s)
        while(j<n):
            if s[j]=='0':
                out+=white
            else:
                white+=1
            j+=1
            
            
        return out