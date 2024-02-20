class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        sum = 0
        prod = 1
        for i in range(len(n)):
          sum += int(n[i])
          prod *= int(n[i])
        return prod - sum 

test = Solution()
print(test.subtractProductAndSum(234))