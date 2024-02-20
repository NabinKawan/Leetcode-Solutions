class Solution(object):
    def longestCommonPrefix(self, strs):
      self.str_list = strs
      common_prefix = False

      if len(self.str_list) == 1:
          return self.str_list[0]
      else:
               #intialization
        first_word = str(self.str_list[0])
        possible_list = []
        current_list = []
        final_prefix = ''

        for i in range(len(first_word)+1):
          possible_prefix = first_word[0:i]
          possible_list.append(possible_prefix)

        for item in possible_list:
          for word in self.str_list:
            if word.startswith(item):
              common_prefix = True
            else:
              common_prefix = False
              break
          if common_prefix:
            current_list.append(item)

        for item in current_list:
          if len(item) > len(final_prefix):
            final_prefix = item
        
        
        return final_prefix
        

        


TestCase1 = Solution()
TestCase2 = Solution()
TestCase3 = Solution()
TestCase4 = Solution()
TestCase5 = Solution()
TestCase6 = Solution()

print(TestCase1.longestCommonPrefix(["flower","flow","flight"]))
print(TestCase2.longestCommonPrefix(["dog","racecar","car"]))
print(TestCase3.longestCommonPrefix(["aaa","aa","aaa"]))
print(TestCase3.longestCommonPrefix(["c","acc","ccc"]))
print(TestCase3.longestCommonPrefix(["a"]))
print(TestCase6.longestCommonPrefix(["a","ab"]))