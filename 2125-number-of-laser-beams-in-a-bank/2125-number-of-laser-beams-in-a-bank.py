class Solution(object):
    def numberOfBeams(self, bank):
        out = 0
        rone=bank[0].count("1")
        for i in bank[1:]:
            rtwo = i.count("1")
            if rtwo != 0:
                out+=rone*rtwo
                rone = rtwo
        return out
            
                
        
        