class Solution(object):
    def transpose(self, matrix):
        self.list = matrix
        transpose_matrix = []
        for i in range(len(self.list[0])):
          new_matrix = []
          for j in range(len(self.list)):
            new_matrix.append(self.list[j][i])
          transpose_matrix.append(new_matrix)
        return transpose_matrix


test = Solution()
print(test.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(test.transpose([[1,2,3],[4,5,6]]))