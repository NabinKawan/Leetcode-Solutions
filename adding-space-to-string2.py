class Solution(object):
    def addSpaces(self, s, spaces):
      str_list = [s[i] for i in range(len(s))]
      new_str = ''
      for items in spaces:
        str_list[items] = ' ' + str_list[items]
      for items in str_list:
        new_str += items
      print(new_str)
      return new_str

test = Solution()
print(test.addSpaces("LeetcodeHelpsMeLearn",[8,13,15]))
print(test.addSpaces( "EnjoyYourCoffee",[5, 9]))
print(test.addSpaces("spacing",[0,1,2,3,4,5,6]))