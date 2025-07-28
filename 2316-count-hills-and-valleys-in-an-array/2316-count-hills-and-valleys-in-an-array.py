class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        out =[nums[0]]
        for i in nums[1:]:
            if i != out[-1]:
                out.append(i)
        v,h = 0,0
        print(out)
        for i in range(1,len(out)-1):
            a,b,c= out[i-1], out[i],out[i+1]
            if a<b and c<b:
                h+=1
            elif b<a and b<c:
                v+=1
        return v+h

        