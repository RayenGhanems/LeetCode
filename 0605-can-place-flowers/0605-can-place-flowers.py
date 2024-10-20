class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        z = 0

        if n == 0 :
            return True

        if len(flowerbed)==1:
            if flowerbed ==[0] and n<=1:
                return True
            return False

        if flowerbed[0] ==0 and flowerbed[1] ==0:
            flowerbed[0] = 1
            n-=1

        if flowerbed[-1] ==0 and flowerbed[-2] ==0:
            flowerbed[-1] = 1
            n-=1

        if n <= 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                z = 0
            else:
                z+=1

            if z == 3:
                n -= 1
                if n <= 0:
                    return True
                z = 1
        return False

        