class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = strs[0]
        for w in strs[1:]:
            i=0
            l=min(len (w),len(out))
            for i in range(l):
                if out[i]!=w[i]:
                    if i ==0:
                        return ""
                    break
                i+=1
            out=out[:i]
        return "".join(str(o) for o in out)