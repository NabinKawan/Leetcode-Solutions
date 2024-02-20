class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
      li = text.split()
      total = 0
      for i in range(len(brokenLetters)):
        for j in range(len(li)):
          if brokenLetters[i] in li[j]:
            li[j] = "!"
      for item in li:
        if item != "!":
          total += 1
      return total


test = Solution()
print(test.canBeTypedWords("leet code" , "e"))