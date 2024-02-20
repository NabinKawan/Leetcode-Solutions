class Solution:
    def countBits(self, n: int):
      self.list = []
      for i in range(n+1):
        binary_num = self.convert_to_binary_(i)
        bits = 0
        for i in range(len(binary_num)):
          bits += int(binary_num[i])
        self.list.append(bits)
      return self.list

    def convert_to_binary_(self , num):
      remainder = ''
      while num != 0 :
        remainder += str(num%2)
        num = num//2
      return remainder[::-1]

test = Solution()
test.countBits(5)