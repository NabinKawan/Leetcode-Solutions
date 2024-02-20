class Solution:
    def searchMatrix(self, matrix , target):
      num_list = []
      for items in matrix:
        for item in items:
          num_list.append(item)
      low = 0
      high = len(num_list)-1
      while low <= high :
        mid = (low + high)// 2
        if num_list[mid] == target:
          return True
        elif num_list[mid] > target:
          high = mid - 1
        else:
          low = mid + 1
      return False

test = Solution()

print(test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]] , 3))
print(test.searchMatrix([[1]],2))
print(test.searchMatrix([[1,3]],3))