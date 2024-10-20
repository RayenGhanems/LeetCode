class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} 
        q =[]

        for i in range(len(s)):
            if s[i] in v:
                q.append(s[i])
        if len(q)<=1:
            return"".join(s)
        for i in range(len(s)):
            if s[i] in v:
                s[i] = q.pop()
        return "".join(s)