class Solution:
    def generate(self, numRows):
      output_row = []
      for i in range(numRows):
        row = []
        for j in range(i+1):
          if j == 0 or j == i:
            row.append(1)
          else:
            num = output_row[i-1][j] + output_row[i-1][j-1]
            row.append(num)
        output_row.append(row)
      return output_row

test = Solution()
print(test.generate(5))