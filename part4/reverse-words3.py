class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split()
        final_str = ''
        for item in words_list:
          final_str += item[::-1] + ' '
        return final_str.rstrip()