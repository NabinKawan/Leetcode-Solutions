class Solution:
    def twoSum(self, numbers, target: int):
        if len(numbers) == 0:
            return None
        i = 0 
        j = 1
        for i in range(len(numbers)):
          for j in range(len(numbers)):
            if i != j and numbers[i] + numbers [j] ==target:
              return [ i+1 , j+1]


test = Solution()
print(test.twoSum([5,25,75],100))