class Solution:
    def generate(self, n: int) -> List[List[int]]:
        out = [[1],[1,1]]
        if n <3:
            return out[:n]
        
        last =out[-1]
        
        for i in range(n-2):
            new =[]
            for j in range(len(last)):
                if j ==0:
                    new.append(last[j])
                else:
                    new.append(last[j]+last[j-1])
            new.append(1)
            last = new
            out.append(new)
        print(out)
        return out
                

        