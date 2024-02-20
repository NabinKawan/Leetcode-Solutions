class Solution:
    def removePalindromeSub(self , s):
        num_of_steps = 0 
        while len(s) != 0:
          last_index = 0
          seq = ""
          for j in range(len(s)):
            word = s[0:j]
            if word == word[::-1]:
              seq = word
            print(word)
            s = s.replace(word , "")
          num_of_steps += 1
        return num_of_steps



test = Solution()
test.removePalindromeSub("abbba")
test.removePalindromeSub("abb")