class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.str = s
        valid_palindromes = []
        for i in range(len(self.str)):
          for j in range(i , len(self.str)+1):
            word = self.str[i:j]
            if len(word) >= 1:
             status = self._check_if_palindrome_(word)
             if status:
                valid_palindromes.append(word)
        print(valid_palindromes)
        return self._return_longest_(valid_palindromes)
    

    def _check_if_palindrome_(self , word):
      return word == word[::-1]
    
    def _return_longest_(self , li):
      longest_word = None
      for word in li:
        if longest_word is None or len(word) > len(longest_word):
          longest_word = word 
      return longest_word




test = Solution()
print(test.longestPalindrome("cbbd"))