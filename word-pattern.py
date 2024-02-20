class Solution(object):
    def wordPattern(self, pattern, s):
      pattern_dict = {}
      words_list = s.split()
      initial_len_check = self.check_matching_len(pattern , words_list)
      if initial_len_check == False:
        return False
      else:
        for i in range(len(pattern)):
          current_letter = pattern[i]
          current_word = words_list[i]
          if current_letter in pattern_dict:
            if pattern_dict[current_letter] != current_word:
              return False
          pattern_dict[current_letter] = current_word
      check_list = []
      for value in pattern_dict.values():
        if value in check_list:
          return False
        else:
          check_list.append(value)
      return True

    def check_matching_len(self, pattern , words_list):
      if len(pattern) == len(words_list) or len(pattern) == 0 or len(words_list) == 0:
        return True
      else:
        return False




test = Solution()
print(test.wordPattern("abba","dog cat cat dog"))
print(test.wordPattern("abba","dog cat cat fish"))
print(test.wordPattern("aaaa","dog cat cat dog"))
print(test.wordPattern("abba","dog dog dog dog"))