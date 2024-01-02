class Solution(object):
    def findMatrix(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1    
        out = []
        
        while dic:
            l = []
            keys_to_remove = []
            for key in dic:
                if dic[key] > 1:
                    dic[key] -= 1
                    l.append(key)
                else:
                    keys_to_remove.append(key)
                    l.append(key)
            
            for key in keys_to_remove:
                del dic[key]

            out.append(l)
        
        return out
