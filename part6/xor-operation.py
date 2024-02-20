class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = [start + 2*i for i in range(n)]
        return result


test = Solution()
print(test.xorOperation(5,0))