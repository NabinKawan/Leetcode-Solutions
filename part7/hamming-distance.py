class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        numx = self.binary(x)
        numy = self.binary(y)
        
        target_len = max(len(numx) , len(numy))
        formated_numx = self._format_binary_(target_len , numx)
        formated_numy = self._format_binary_(target_len , numy)
        hammingDistance = 0

        for i in range(target_len):
          if formated_numx[i] != formated_numy[i]:
            hammingDistance += 1
        return hammingDistance

        
    
    def binary(self , num , result = ""):
      if num == 0:
        return result[::-1]
      result += str(num%2)
      num = num//2
      return self.binary(num , result)
    
    def _format_binary_(self , target_len , binary):
      if len(binary) == target_len:
        return binary
      else:
        prefix = "0" * (target_len - len(binary))
        binary = prefix + binary
        return binary


test = Solution()

print(test.hammingDistance(1,4))