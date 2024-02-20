class Solution:
    def fib(self, n: int):
        if n <= 1:
          return n
        else:
          return self.fib(n-1) + self.fib(n-2)
    

test = Solution()
print(test.fib(4))