class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        icecreams = 0
        for i in range(len(costs)):
            if coins == 0:
                break
            if coins >= costs[i]:
                coins -= costs[i]
                icecreams += 1
        return icecreams
