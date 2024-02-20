class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        str_list = [s[i] for i in range(len(s))]
        current_vowels = []
        new_word = ''
        j = 0
        for i in range(len(str_list)):
          if str_list[i]  in vowels:
            current_vowels.append(s[i])
        current_vowels.reverse()
        for i in range(len(s)):
          if str_list[i] in vowels:
            str_list[i] = current_vowels[j]
            j += 1
        for item in str_list:
          new_word += item
        return new_word
        

            


test = Solution()
print(test.reverseVowels("hello"))
print(test.reverseVowels("leetcode"))