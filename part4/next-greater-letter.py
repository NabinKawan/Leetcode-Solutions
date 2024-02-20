class Solution:
    def nextGreatestLetter(self, letters, target):
       self.letters = letters
       self.letters.append(target)
       first_word = self.letters[0]
       self.letters.sort()
       next_greater_elm = None
       for i in range(len(self.letters)):
        if self.letters[i] == target:
          try:
            j = 1
            while next_greater_elm is None or next_greater_elm == self.letters[i]:
              next_greater_elm = self.letters[i+j]
              j+=1
            return next_greater_elm
          except:
            return first_word


test = Solution()
print(test.nextGreatestLetter(["c","f","j"],"c"))