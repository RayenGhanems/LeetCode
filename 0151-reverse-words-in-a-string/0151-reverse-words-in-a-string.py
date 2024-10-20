class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        out = []
        q = []

        while s[-1]==" ":
            s.pop()
        while s[0]==" ":
            s.pop(0)

        for i in s:
            if i ==" ":
                if q:
                    out.append("".join(q)) 
                if out[-1] != " ":
                    out.append(" ") 
                q = []
            else:
                q.append(i)
        out.append("".join(q))
        
        return "".join(out[::-1])