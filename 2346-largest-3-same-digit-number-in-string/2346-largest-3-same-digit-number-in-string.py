class Solution:
    def largestGoodInteger(self, num: str) -> str:
        out=-1
        for i in range(len(num)-2):
            j=i+2
            if num[i]==num[j] and num[i]==num[i+1]:
                out =max(out,int(num[i]*3))
        if out>0:
            return str(out)
        elif out ==0:
            return "000"
        return ""
