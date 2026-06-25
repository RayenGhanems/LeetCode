class Solution:
    def countMajoritySubarrays(self, nums: List[int], t: int) -> int:
        L, N= [], len(nums)
        for i, x in enumerate(nums):
            if x == t:
                L.append(i)
        l = len(L)
        if l<2:        ## if it is 0 or 1 then it is impossible for the output to be other than 0 or 1 
            return l
        
        out ,nj , j0= 0,L[0], 0
        for i in range(N):
            n, tc = 0, 0
            j = j0 
            while j < l:
                n = L[j]-i +1
                tc += 2     ## add 2 instead of doing n//2 or whatever just simpler
                if tc > n:
                    if l>j+1:
                        out+=min(N-L[j], (tc-n), L[j+1]-L[j]) 
                    else:
                        out+=min(N-L[j], (tc-n)) 

                     ## so that we dont count subarrays that connot possible exist or instead of counting them twice with since we will count them  with L[j=1]                    
                j+=1
            if i == nj:     ## so that we dont check the targets that are before i
                j0 +=1 
                if j0>=l:
                    break
                nj = L[j0]

        return out
            