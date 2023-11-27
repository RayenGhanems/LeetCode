class Solution(object):
    def garbageCollection(self, Garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        m,p,g,pm,pp,pg=Garbage[0].count("M"),Garbage[0].count("P"),Garbage[0].count("G"),0,0,0
        for i in range(len(travel)):
            M=Garbage[i+1].count("M")
            P=Garbage[i+1].count("P")
            G=Garbage[i+1].count("G")
            if M:
                while(pm<=i):
                    m+=travel[pm]
                    pm+=1
                m+=M
            if P:
                while(pp<=i):
                    p+=travel[pp]
                    pp+=1
                p+=P
            if G:
                while(pg<=i):
                    g+=travel[pg]
                    pg+=1
                g+=G
        return m+g+p