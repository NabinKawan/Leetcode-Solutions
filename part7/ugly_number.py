class Solution:
    def isUgly(self, n: int) -> bool:
        self.ugly_prime = {2,3,5}
        for i in range(n):
          if n% i ==0:
            if i not in self.ugly_prime:
              return False
        return True
