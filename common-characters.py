class Solution:
    def commonChars(self, words):
      word = words[0]
      common_list = []
      for char in word:
        common = True
        for i in range(1, len(words)):
          if char not in words[i]:
            common = False
            break
        if common:
          common_list.append(char)
          for i in range(len(words)):
            words[i] = words[i].replace(char , '' , 1)
      return common_list




test = Solution()
test.commonChars(["bella","label","roller"])