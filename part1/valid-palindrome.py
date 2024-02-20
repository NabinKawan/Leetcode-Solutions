class Solution(object):
    def isPalindrome(self, s):
      string_list = s.split()
      joined_string = ''

      for item in string_list:
        for i in range(len(item)):
          if item[i].isalnum():
            joined_string += item[i].lower()
      
      reversed_string = joined_string[::-1]

      if reversed_string == joined_string :
        return True
      else:
        return False


test = Solution()
#print(test.isPalindrome("A man, a plan, a canal: Panama"))
#print(test.isPalindrome("race a car"))
#print(test.isPalindrome("" ""))

print(test.isPalindrome("0P"))