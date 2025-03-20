class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = nums.count(0)
        if n==0:
            return 0
        if n ==1:
            return -1
        def change(l: List[int]) -> List[int]:
            for i in range(len(l)):
                l[i] = 0 if l[i]==1 else 1
            return l

        s = 0
        f = len(nums) -1
        i = 0
        while nums[s] == 1:
            s+=1
        while nums[f] ==1:
            f-=1
        
        while f>s+1:
            
            if nums[s]==0:
                nums[s:s+3] = change(nums[s:s+3])
                i+=1
            s+=1
        print(nums)
        return i if (nums.count(0)==0) else -1