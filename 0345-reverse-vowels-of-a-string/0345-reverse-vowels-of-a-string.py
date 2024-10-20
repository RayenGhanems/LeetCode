class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} 
        q =[]

        for i in range(len(s)):
            if s[i] in v:
                q.append(s[i])
        for i in range(len(s)):
            if s[i] in v:
                s[i] = q.pop()
        return "".join(s)