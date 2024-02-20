class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel_list = ['a','e','i','o','u','A','E','I','O','U']
        words_list = sentence.split()
        new_sentence = ''
        for i in range(len(words_list)):
           modified_word = ''
           current_word = words_list[i]
           starting_vowel =  self._starts_with_vowel(current_word , vowel_list)
           if starting_vowel:
            current_word += 'ma'
           else:
             first_letter = current_word[0]
             current_word = current_word[1:len(current_word)]
             current_word += first_letter
             current_word += 'ma'
           for j in range(i+1):
             current_word += 'a'
           if i != len(words_list)-1:
            new_sentence += current_word + ' '
           else:
             new_sentence += current_word
        return new_sentence
        
        
    def _starts_with_vowel(self, word , list):
            for vowel in list:
                if word.startswith(vowel):
                    return True
            return False

test = Solution()
test.toGoatLatin("I speak Goat Latin")



test = Solution()
test.toGoatLatin("I speak Goat Latin")