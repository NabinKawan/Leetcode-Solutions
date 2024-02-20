class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        self.my_dict = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
        num1 = self._return_num_value_(firstWord)
        num2 = self._return_num_value_(secondWord)
        num3 = self._return_num_value_(targetWord)
        return num1 + num2 == num3
    
    def _return_num_value_(self , word):
      total_val = ""
      for i in range(len(word)):
        total_val +=str(self.my_dict[word[i]])
      return int(total_val)

test = Solution()
print(test.isSumEqual("acb","cba","cdb"))