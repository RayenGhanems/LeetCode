class Solution:
    def maxDifference(self, st: str) -> int:
        me,mo=inf,0
        s = set(st)
        for i in s:
            m = st.count(i)
            if m%2==0:
                me=min(m,me)
            else:
                mo=max(m,mo)
        return mo-me


        