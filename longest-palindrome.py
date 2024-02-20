class Solution:
    def longestPalindrome(self, s: str) -> int:
        possible_words = []
        palindromes = {}
        for i in range(len(s)+1):
          possible_words.append(s[0:i])
        for item in possible_words:
          print(item , item[::-1])
          if item == item[::-1]:
            palindromes[item] = len(item)
        print(palindromes)


test = Solution()
print(test.longestPalindrome("abccccdd"))