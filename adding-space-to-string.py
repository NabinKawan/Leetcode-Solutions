class Solution(object):
    def addSpaces(self, s, spaces):
      new_str = ''
      j = 0
      current_val = spaces[j]
      for i in range(len(s)):
        if i == spaces[j]:
          new_str += ' ' + s[i]
          if j < len(spaces)-1:
            j +=1
        else:
          new_str += s[i]
      return new_str



test = Solution()
print(test.addSpaces("LeetcodeHelpsMeLearn",[8,13,15]))
print(test.addSpaces( "EnjoyYourCoffee",[5, 9]))