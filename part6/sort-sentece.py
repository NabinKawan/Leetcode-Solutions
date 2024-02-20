class Solution:
    def sortSentence(self, s: str) -> str:
        final_str = ""
        strlist = [item[::-1] for item in s.split()]
        strlist.sort()
        result = [item[1::] for item in strlist]
        for i in range(len(result)):
          word = result[i]
          word = word[::-1]
          if i == len(result)-1:
            final_str += word
          else:
            final_str += word + " "
        return final_str


test = Solution()
print(test.sortSentence("is2 sentence4 This1 a3"))