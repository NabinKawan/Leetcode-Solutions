class Solution:
    def isUgly(self, n: int) -> bool:
      prime_collection = []
      half_point = n//2

      for i in range(1,half_point):
        if n%i == 0 :
          prime_collection.append(i)
    
      print(prime_collection)

test = Solution()
print(test.isUgly(14))
