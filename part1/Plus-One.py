class Solution(object):
    def plusOne(self, digits):
      number = ''
      for item in digits:
        number += str(item)
      new_number = str(int(number)+1)
      list2 = [int(new_number[i]) for i in range(len(new_number))]
      return list2

test = Solution()
print(test.plusOne([1,2,3]))