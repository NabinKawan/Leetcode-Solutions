class Solution(object):
    def reverseWords(self, s):
        string_list = s.split()
        final_string = ''
        i = len(string_list)-1
        while i != -1 :
          if i == 0 :
            final_string  += string_list[0]
          else:
            final_string += string_list[i] + ' '
          i -= 1
        return final_string


test = Solution()
test.reverseWords("hello world this is josrph")

