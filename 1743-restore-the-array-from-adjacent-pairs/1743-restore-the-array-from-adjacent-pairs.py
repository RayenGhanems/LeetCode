class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        temp={}
        first=0
        for i in adjacentPairs :
            temp.setdefault(i[0],[]).append(i[1])
            temp.setdefault(i[1],[]).append(i[0])
        
        for i in temp.keys() :
            if len(temp[i])==1:
                first=i
                break
        
        prev=first
        nextt=temp[first][0]
        v=[first,nextt]
        for  i in range(len(adjacentPairs)-1) :
            t=temp[nextt]
            if t[0]!=prev:
                v.append(t[0])
                prev=nextt
                nextt=t[0]
            elif len(t)>1 :
                v.append(t[1])
                prev=nextt
                nextt=t[1]
            
        
        return v
                


        