class Solution(object):
    def reverseOnlyLetters(self, s):
        self.letters = []
        self.not_letters = []
        final_str = ''
        for i in range(len(s)):
          if s[i].isalpha():
            self.letters.append(s[i])
          else:
            self.not_letters.append((s[i],i))
        self.letters.reverse()
        for item in self.not_letters:
          self.letters.insert(item[1] , item[0])
        for item in self.letters:
          final_str += item
        return final_str


test = Solution()
test.reverseOnlyLetters("ab-cd")

