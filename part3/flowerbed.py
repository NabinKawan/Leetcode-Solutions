class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if flowerbed == [0] and n == 1:
            return True
        for i in range(n):  
            flower_placed = False
            for i in range(len(flowerbed)-1):
                if flowerbed[0] == 0 and flowerbed[1] == 0 :
                    flowerbed[0] = 1 
                    flower_placed = True
                    break
                elif flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0 :
                    flowerbed[-1] = 1
                    flower_placed = True
                    break
                elif flowerbed[i] == 0:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        flower_placed = True
                        break
            if flower_placed == False:
                return False
        return True


test = Solution()
print(test.canPlaceFlowers([0,0,1,0 ],2))
        