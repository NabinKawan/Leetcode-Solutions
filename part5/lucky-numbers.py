class Solution:
    def luckyNumbers (self, matrix):
      luckyNumbers = []
      for i in range(len(matrix[0])):
        min_num = None
        min_row = None
        for j in range(len(matrix)):
          if min_num is None:
            min_num = matrix[j][i]
          if min_row is None:
            min_row = j
          elif min_num < matrix[j][i]:
            min_num = matrix[j][i]
            min_row = j
        min_status = self._check_if_num_is_smallest_in_row(min_num , min_row , matrix )
        if min_status :
          luckyNumbers.append(min_num)
      return luckyNumbers
    
    def _check_if_num_is_smallest_in_row(self , num , index , matrix):
      return min(matrix[index]) == num
          




test = Solution()
test.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])
test.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])
test.luckyNumbers([[7,8],[1,2]])