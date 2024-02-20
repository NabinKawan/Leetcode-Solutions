class Solution:
    def mostCommonWord(self, paragraph , banned):
      self.dict = {}
      self.banned = banned
      for word in paragraph.split():
        word = word.lower()
        word = word.replace('.', '')
        word = word.replace('!','') 
        word = word.replace('?', '')
        word = word.replace(';','')
        if word[-1] == ',':
         word = word[0:len(word)-1]
        if ',' in word:
          for i in range(len(word)):
            if word[i].isalpha():
              self._apppend_to_dict_(word[i])
        else:
          self._apppend_to_dict_(word)
      max = self.find_max()
      return max
    
    
    def _apppend_to_dict_(self , word):
        if word in self.dict:
          self.dict[word] += 1
        elif word not in self.banned:
          self.dict[word] = 1
    

    def find_max(self):
      max_value = 0
      max_word = ''
      for key,value in self.dict.items():
        if value > max_value:
          max_value = value
          max_word = key
      print(self.dict)
      return max_word

test = Solution()
print(test.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
print(test.mostCommonWord("a, a, a, a, b,b,b,c, c" , ["a"]))

print(test.mostCommonWord("L, P! X! C; u! P? w! P. G, S? l? X? D. w? m? f? v, x? i. z; x' m! U' M! j? V; l. S! j? r, K. O? k? p? p, H! t! z' X! v. u; F, h; s? X? K. y, Y! L; q! y? j, o? D' y? F' Z; E? W; W' W! n! p' U. N; w? V' y! Q; J, o! T? g? o! N' M? X? w! V. w? o' k. W. y, k; o' m! r; i, n. k, w; U? S? t; O' g' z. V. N? z, W? j! m? W! h; t! V' T! Z? R' w, w? y? y; O' w; r? q. G, V. x? n, Y; Q. s? S. G. f, s! U? l. o! i. L; Z' X! u. y, Q. q; Q, D; V. m. q. s? Y, U; p? u! q? h? O. W' y? Z! x! r. E, R, r' X' V, b. z, x! Q; y, g' j; j. q; W; v' X! J' H? i' o? n, Y. X! x? h? u; T? l! o? z. K' z' s; L? p? V' r. L? Y; V! V' S. t? Z' T' Y. s? i? Y! G? r; Y; T! h! K; M. k. U; A! V? R? C' x! X. M; z' V! w. N. T? Y' w? n, Z, Z? Y' R; V' f; V' I; t? X? Z; l? R, Q! Z. R. R, O. S! w; p' T. u? U! n, V, M. p? Q, O? q' t. B, k. u. H' T; T? S; Y! S! i? q! K' z' S! v; L. x; q; W? m? y, Z! x. y. j? N' R' I? r? V! Z; s, O? s; V, I, e? U' w! T? T! u; U! e? w? z; t! C! z? U, p' p! r. x; U! Z; u! j; T! X! N' F? n! P' t, X. s; q'",["m","i","s","w","y","d","q","l","a","p","n","t","u","b","o","e","f","g","c","x"]))