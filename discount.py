class Solution:
    def finalPrices(self, prices):
        result = []
        for i in range(len(prices)):
            inserted = False
            for j in range(i+1 , len(prices)):
                if j > i and prices[j] <= prices[i] and inserted == False:
                    print(prices[j] , prices[i])
                    result.append(prices[i]-prices[j])
                    inserted = True
                    break
            if not inserted:
                 print(prices[i])
                 result.append(prices[i])
        return result


test = Solution()
print(test.finalPrices([8,4,6,2,3]))