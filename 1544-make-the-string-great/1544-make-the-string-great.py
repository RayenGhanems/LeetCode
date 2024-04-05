class Solution:
    def makeGood(self, s: str) -> str:
        out=s[0]
        for i in s[1:]:
            if len(out)==0:
                out+=i
            else:
                if out[-1].lower()==i.lower() and out[-1]!=i:
                    out=out[:-1]
                else:
                    out+=i
        return out