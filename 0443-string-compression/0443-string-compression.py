class Solution:
    def compress(self, chars: List[str]) -> int:
        out = []
        n=0
        l=chars[0]
        for i in chars:
            if i == l:
                n+=1
            else:
                out.append(l)
                if n > 1:
                    if n <10:
                        out.append(str(n))
                    else:
                        a = list(str(n))
                        for j in a:
                            out.append(str(j))
                l=i
                n=1
        out.append(l)
        if n > 1:
            if n <10:
                out.append(str(n))
            else:
                a = list(str(n))
                for j in a:
                    out.append(str(j))
               
        chars[:] = out
        return len(out)
